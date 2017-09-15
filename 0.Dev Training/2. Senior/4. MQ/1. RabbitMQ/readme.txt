. 参见:

      http://www.cnblogs.com/kerwinC/p/5967584.html

      http://www.jb51.net/article/75647.htm

. 一、概念

      Connection: 一个TCP的连接. Producer 和 Consumer 都是通过TCP连接到 RabbitMQ Server 的. 程序的起始处就是建立这个TCP连接

      Channels: 虚拟连接. 建立在上述的TCP连接中. 数据流动都是在Channel中进行的. 一般情况是程序起始建立TCP连接, 第二步就是建立这个Channel。

。二、队列

      首先建立一个Connection, 然后建立Channels, 在channel上建立队列

      建立时指定durable 参数为真, 队列将持久化; 指定exclusive 为真, 队列为临时队列, 关闭consumer 后该队列将不再存在, 一般情况下建立临时队列并不指定队列名称, rabbitmq 将随机起名, 通过 result.method.queue 来获取队列名:

          result = channel.queue_declare( exclusive = True )
          
          result.method.queue

      区别: durable 是队列持久化与否, 如果是真, 队列将在 rabbitmq 服务重启后仍存在, 如果是假, rabbitmq 服务重启前不会消失, 与consumer 关闭与否无关;

      而exclusive 是建立临时队列, 当consumer关闭后, 该队列就会被删除

. 三、exchange 和bind

      Exchange 中的durable参数指定exchange是否持久化, exchange 参数指定exchange名称, type 指定exchange类型. Exchange类型有 direct, fanout 和 topic.

      Bind 是将exchange 与queue 进行关联, exchange 参数与 queue 参数分别指定要进行bind的exchange 和 queue , routing_key 为可选参数.

      Exchange 的三种模式:

      Direct:

          任何发送到Direct Exchange 的消息都会被转发到 routing_key 中指定的Queue

          1. 一般情况下可以使用rabbitMQ自带的Exchange: "" (该 Exchange 的名字为空字符串)   

          2. 这种模式下不需要将Exchange 进行任何绑定(bind)操作:

          3. 消息传递时需要一个"routing_key", 可以简单的理解为要发送到的队列名字;

          4. 如果vhost中不存在routing_key  中指定的队列名, 则该消息会被抛弃.

          Demo 中 虽然声明了一个exchange='yanfa' 和 queue ='anheng' 的bind, 但是在后面发送消息时并没有使用该exchange和bind, 而是采用了direct的模式, 没有指定exchange，而是指定了routing_key 的名称为队列名, 消息将发送到指定队列.

          如果一个exchange声明为direct, 并且bind中指定了routing_key, 那么发送消息时需要同时指明该exchange和routing_key。

      Fanout:

          任何发送到 Fanout Exchange 的消息都会被转发到与Exchange 绑定(Binding)的所有Queue上

          1. 可以理解为路由表的模式

          2. 这种模式不需要routing_key

          3. 这种模式需要提前将Exchange 与Queue 进行绑定, 一个Exchange可以绑定多个Queue, 一个Queue可以同多个Exchange进行绑定。

          4. 如果接受到消息的Exchange 没有与任何Queue 绑定, 则消息会被抛弃.

          Demo 中创建了一个将一个exchange 和 一个queue进行fanout类型的bind. 但是发送消息时没有用到它, 如果要用到它, 只要在发送消息时指定该exchange 的名称即可, 该exchange 就会将消息发送到所有和它bind 的队列中. 在fanout模式下, 指定的routing_key是无效的.

      Topoic:

          任何发送到Topic Exchange 消息都会被转发到所有关心routing_key 中指定话题的Queue上

          1. 这种模式较为复杂, 简单来说, 就是每个队列都有其关心的主题, 所有的消息都带有一个"标题"(routing_key), Exchange会将消息转发到所有关注主题能与routing_key模糊匹配的队列.

          2. 这种模式需要routing_key, 也许要提前绑定Exchange 与 Queue.

          3. 在进行绑定时, 要提供一个该队列关心的主题, 如"#.log" 表示该队列关心所有涉及log的消息(一个routing_key为"MQ.log.error"的消息会被转发到该队列)

          4. "#" 表示0个或若干个关键字, "*" 表示一个关键字. 如"log.*"能与"log.warn"匹配, 无法与"log.warn.timeout"匹配; 但是"log.#"能与上述两者匹配.

          5. 同样, 如果Exchange 没有发现能够与routing_key 匹配的Queue, 则会抛弃次消息.

. 四、任务分发

  1. Rabbitmq 的任务是循环分发的. 如果开启两个consumer, producer 发送的信息是轮流发送到两个consumer的

  2. 在producer 端使用cha.basic_publish()来发送消息, 其中body 参数就是要发送的消息, properties = pika.BasicProperties(delivery_mode=2,)启用消息持久化, 可以防止RabbitMQ ZServer 重启或者crash 引起的数据丢失.

  3. 在接收端使用cha.basic_consume() 无限循环监听, 如果设置no-ack参数为真, 每次Consumer 接到数据后, 而不管是否处理完成, RabbitMQ Server 会立即把这个Message标记为完成, 然后从queue 中删除了.  为了保证数据不被丢失, RabbitMQ Server 会立即把这个Message标记为完成, 然后从queue 中删除了. 为了保证数据不被丢失, RabbitMQ支持消息确认机制, 即acknowledgments. 为了保证数据能被正确处理而不仅仅是被Consumer收到, 那么我们不能采用no-ack. 而应该是在处理完数据后发送ack.

     在处理数据后发送的ack, 就是告诉RabbitMQ 数据已经被接收, 处理完成, RabbitMQ可以去安全的删除它了. 如果Consumer 退出了但是没有发送ack, 那么RabbitMQ就会把这个Message发送到下一个Consumer. 这样就保证了在Consumer 异常退出的情况下数据也不会丢失.

     这里并没有用到超时机制. RabbitMQ仅仅通过Consumer 的连接中断来确认该Message并没有被正确处理. 也就是说, RabbitMQ给了Consumer 足够长德时间来做数据处理.

     Demo 的callback 方法中ch.basic_ack( delivery_tag = method.delivery_tag) 告诉rabbitmq 消息已经正确处理. 如果没有这条代码, Consumer 退出时, Message会重新分发. 然后 RabbitMQ 会占用越来越多的内存, 由于RabbitMQ 会长时间运行, 因此这个"内存泄漏"是致命的. 去调试这种错误, 可以通过一个命令打印un-acked Messages:

       sudo rabbitmqctl list_queues name messages_ready messages_unacknowledged

   4. 公平分发: 设置 cha.basic_qos( prefetch_count=1), 这样RabbitMQ就会使得每个Consumer在同一个时间点最多处理一个Message. 换句话说, 在接收到该Consumer 的ack前, 它不会将新的Message分发给它.

. 五、注意

  生产者和消费者都应该声明建立队列, 网上教程上说第二次创建如果参数和第一次不一样, 那么该操作虽然成功, 但是queue 的属性并不会被修改.

  可能因为版本问题, 在我的测试中如果第二次声明建立的队列属性和第一次不完全相同, 将报类似这种错406, "PRECONDITION_FAILED - parameters for queue 'anheng' in vhost '/' not equivalent"

  如果是exchange第二次创建属性不同, 将报这种错406, "PRECONDITION_FAILED - cannot redeclare exchange 'yanfa' in vhost '/' with different type, durable, internal or autodelete value"

  如果第一次声明建立队列也出现这个错误, 说明之前存在名字相同的队列且本次声明的某些属性和之前的声明不同, 可通过命令sudo rabbitmqctl list_queues 查看当前有哪些队列. 解决方法是声明建立另一个名称的队列或删除原有队列, 如果原有队列是非持久化的, 可以通过重启rabbitmq 服务删除原有队列, 如果原有队列是持久化的, 只能删除它所在的vhost, 然后再重建vhost, 再设置vhost的权限(先确认该vhost 中没有其他有用队列).

  sudo rabbitmqctl delete_vhost /

  sudo rabbitmqctl add_vhost /

  sudo rabbitmqctl set_permissions -p / username '.*' '.*' '.*'

  