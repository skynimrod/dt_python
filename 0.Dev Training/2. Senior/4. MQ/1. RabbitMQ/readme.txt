. �μ�:

      http://www.cnblogs.com/kerwinC/p/5967584.html

      http://www.jb51.net/article/75647.htm

. һ������

      Connection: һ��TCP������. Producer �� Consumer ����ͨ��TCP���ӵ� RabbitMQ Server ��. �������ʼ�����ǽ������TCP����

      Channels: ��������. ������������TCP������. ��������������Channel�н��е�. һ������ǳ�����ʼ����TCP����, �ڶ������ǽ������Channel��

����������

      ���Ƚ���һ��Connection, Ȼ����Channels, ��channel�Ͻ�������

      ����ʱָ��durable ����Ϊ��, ���н��־û�; ָ��exclusive Ϊ��, ����Ϊ��ʱ����, �ر�consumer ��ö��н����ٴ���, һ������½�����ʱ���в���ָ����������, rabbitmq ���������, ͨ�� result.method.queue ����ȡ������:

          result = channel.queue_declare( exclusive = True )
          
          result.method.queue

      ����: durable �Ƕ��г־û����, �������, ���н��� rabbitmq �����������Դ���, ����Ǽ�, rabbitmq ��������ǰ������ʧ, ��consumer �ر�����޹�;

      ��exclusive �ǽ�����ʱ����, ��consumer�رպ�, �ö��оͻᱻɾ��

. ����exchange ��bind

      Exchange �е�durable����ָ��exchange�Ƿ�־û�, exchange ����ָ��exchange����, type ָ��exchange����. Exchange������ direct, fanout �� topic.

      Bind �ǽ�exchange ��queue ���й���, exchange ������ queue �����ֱ�ָ��Ҫ����bind��exchange �� queue , routing_key Ϊ��ѡ����.

      Exchange ������ģʽ:

      Direct:

          �κη��͵�Direct Exchange ����Ϣ���ᱻת���� routing_key ��ָ����Queue

          1. һ������¿���ʹ��rabbitMQ�Դ���Exchange: "" (�� Exchange ������Ϊ���ַ���)   

          2. ����ģʽ�²���Ҫ��Exchange �����κΰ�(bind)����:

          3. ��Ϣ����ʱ��Ҫһ��"routing_key", ���Լ򵥵����ΪҪ���͵��Ķ�������;

          4. ���vhost�в�����routing_key  ��ָ���Ķ�����, �����Ϣ�ᱻ����.

          Demo �� ��Ȼ������һ��exchange='yanfa' �� queue ='anheng' ��bind, �����ں��淢����Ϣʱ��û��ʹ�ø�exchange��bind, ���ǲ�����direct��ģʽ, û��ָ��exchange������ָ����routing_key ������Ϊ������, ��Ϣ�����͵�ָ������.

          ���һ��exchange����Ϊdirect, ����bind��ָ����routing_key, ��ô������Ϣʱ��Ҫͬʱָ����exchange��routing_key��

      Fanout:

          �κη��͵� Fanout Exchange ����Ϣ���ᱻת������Exchange ��(Binding)������Queue��

          1. �������Ϊ·�ɱ��ģʽ

          2. ����ģʽ����Ҫrouting_key

          3. ����ģʽ��Ҫ��ǰ��Exchange ��Queue ���а�, һ��Exchange���԰󶨶��Queue, һ��Queue����ͬ���Exchange���а󶨡�

          4. ������ܵ���Ϣ��Exchange û�����κ�Queue ��, ����Ϣ�ᱻ����.

          Demo �д�����һ����һ��exchange �� һ��queue����fanout���͵�bind. ���Ƿ�����Ϣʱû���õ���, ���Ҫ�õ���, ֻҪ�ڷ�����Ϣʱָ����exchange �����Ƽ���, ��exchange �ͻὫ��Ϣ���͵����к���bind �Ķ�����. ��fanoutģʽ��, ָ����routing_key����Ч��.

      Topoic:

          �κη��͵�Topic Exchange ��Ϣ���ᱻת�������й���routing_key ��ָ�������Queue��

          1. ����ģʽ��Ϊ����, ����˵, ����ÿ�����ж�������ĵ�����, ���е���Ϣ������һ��"����"(routing_key), Exchange�Ὣ��Ϣת�������й�ע��������routing_keyģ��ƥ��Ķ���.

          2. ����ģʽ��Ҫrouting_key, Ҳ��Ҫ��ǰ��Exchange �� Queue.

          3. �ڽ��а�ʱ, Ҫ�ṩһ���ö��й��ĵ�����, ��"#.log" ��ʾ�ö��й��������漰log����Ϣ(һ��routing_keyΪ"MQ.log.error"����Ϣ�ᱻת�����ö���)

          4. "#" ��ʾ0�������ɸ��ؼ���, "*" ��ʾһ���ؼ���. ��"log.*"����"log.warn"ƥ��, �޷���"log.warn.timeout"ƥ��; ����"log.#"������������ƥ��.

          5. ͬ��, ���Exchange û�з����ܹ���routing_key ƥ���Queue, �����������Ϣ.

. �ġ�����ַ�

  1. Rabbitmq ��������ѭ���ַ���. �����������consumer, producer ���͵���Ϣ���������͵�����consumer��

  2. ��producer ��ʹ��cha.basic_publish()��������Ϣ, ����body ��������Ҫ���͵���Ϣ, properties = pika.BasicProperties(delivery_mode=2,)������Ϣ�־û�, ���Է�ֹRabbitMQ ZServer ��������crash ��������ݶ�ʧ.

  3. �ڽ��ն�ʹ��cha.basic_consume() ����ѭ������, �������no-ack����Ϊ��, ÿ��Consumer �ӵ����ݺ�, �������Ƿ������, RabbitMQ Server �����������Message���Ϊ���, Ȼ���queue ��ɾ����.  Ϊ�˱�֤���ݲ�����ʧ, RabbitMQ Server �����������Message���Ϊ���, Ȼ���queue ��ɾ����. Ϊ�˱�֤���ݲ�����ʧ, RabbitMQ֧����Ϣȷ�ϻ���, ��acknowledgments. Ϊ�˱�֤�����ܱ���ȷ������������Ǳ�Consumer�յ�, ��ô���ǲ��ܲ���no-ack. ��Ӧ�����ڴ��������ݺ���ack.

     �ڴ������ݺ��͵�ack, ���Ǹ���RabbitMQ �����Ѿ�������, �������, RabbitMQ����ȥ��ȫ��ɾ������. ���Consumer �˳��˵���û�з���ack, ��ôRabbitMQ�ͻ�����Message���͵���һ��Consumer. �����ͱ�֤����Consumer �쳣�˳������������Ҳ���ᶪʧ.

     ���ﲢû���õ���ʱ����. RabbitMQ����ͨ��Consumer �������ж���ȷ�ϸ�Message��û�б���ȷ����. Ҳ����˵, RabbitMQ����Consumer �㹻����ʱ���������ݴ���.

     Demo ��callback ������ch.basic_ack( delivery_tag = method.delivery_tag) ����rabbitmq ��Ϣ�Ѿ���ȷ����. ���û����������, Consumer �˳�ʱ, Message�����·ַ�. Ȼ�� RabbitMQ ��ռ��Խ��Խ����ڴ�, ����RabbitMQ �᳤ʱ������, ������"�ڴ�й©"��������. ȥ�������ִ���, ����ͨ��һ�������ӡun-acked Messages:

       sudo rabbitmqctl list_queues name messages_ready messages_unacknowledged

   4. ��ƽ�ַ�: ���� cha.basic_qos( prefetch_count=1), ����RabbitMQ�ͻ�ʹ��ÿ��Consumer��ͬһ��ʱ�����ദ��һ��Message. ���仰˵, �ڽ��յ���Consumer ��ackǰ, �����Ὣ�µ�Message�ַ�����.

. �塢ע��

  �����ߺ������߶�Ӧ��������������, ���Ͻ̳���˵�ڶ��δ�����������͵�һ�β�һ��, ��ô�ò�����Ȼ�ɹ�, ����queue �����Բ����ᱻ�޸�.

  ������Ϊ�汾����, ���ҵĲ���������ڶ������������Ķ������Ժ͵�һ�β���ȫ��ͬ, �����������ִ�406, "PRECONDITION_FAILED - parameters for queue 'anheng' in vhost '/' not equivalent"

  �����exchange�ڶ��δ������Բ�ͬ, �������ִ�406, "PRECONDITION_FAILED - cannot redeclare exchange 'yanfa' in vhost '/' with different type, durable, internal or autodelete value"

  �����һ��������������Ҳ�����������, ˵��֮ǰ����������ͬ�Ķ����ұ���������ĳЩ���Ժ�֮ǰ��������ͬ, ��ͨ������sudo rabbitmqctl list_queues �鿴��ǰ����Щ����. �������������������һ�����ƵĶ��л�ɾ��ԭ�ж���, ���ԭ�ж����Ƿǳ־û���, ����ͨ������rabbitmq ����ɾ��ԭ�ж���, ���ԭ�ж����ǳ־û���, ֻ��ɾ�������ڵ�vhost, Ȼ�����ؽ�vhost, ������vhost��Ȩ��(��ȷ�ϸ�vhost ��û���������ö���).

  sudo rabbitmqctl delete_vhost /

  sudo rabbitmqctl add_vhost /

  sudo rabbitmqctl set_permissions -p / username '.*' '.*' '.*'

  