. 参见:

   https://www.djangoproject.com/download/

   http://blog.csdn.net/column/details/djangonote.html

   https://docs.djangoproject.com/en/1.10/intro/tutorial01/

. 1. 安装 Django

     pip install Django==1.10.1

. 2. 创建 Django 项目

     进入相对应的开发环境后再创建项目, 以后都是这样.

     django-admin.py startproject Project1    

     Project1 是项目名称. 上面的命令会创建Project1目录以及其下面的一些子目录和文件.

(env2) F:\F_3_test\3_Python>cd Project1

(env2) F:\F_3_test\3_Python\Project1>dir
 驱动器 F 中的卷是 文档
 卷的序列号是 000E-B5CB

 F:\F_3_test\3_Python\Project1 的目录

2016/10/03  18:23    <DIR>          .
2016/10/03  18:23    <DIR>          ..
2016/10/03  18:23    <DIR>          Project1
2016/10/03  18:23               804 manage.py
               1 个文件            804 字节
               3 个目录 133,223,604,224 可用字节


. 3. 创建应用

     进入项目目录  Project1, 运行

(env2) F:\F_3_test\3_Python\Project1>manage.py startapp app1

(env2) F:\F_3_test\3_Python\Project1>dir
 驱动器 F 中的卷是 文档
 卷的序列号是 000E-B5CB

 F:\F_3_test\3_Python\Project1 的目录

2016/10/03  18:25    <DIR>          .
2016/10/03  18:25    <DIR>          ..
2016/10/03  18:25    <DIR>          Project1
2016/10/03  18:25    <DIR>          app1
2016/10/03  18:23               804 manage.py
               1 个文件            804 字节
               4 个目录 133,223,596,032 可用字节

. 4. 测试之前的操作是否成功.

(env2) F:\F_3_test\3_Python\Project1>manage.py runserver localhost:8000
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you
 apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.  ---------------------------------------> 这儿提示了如果要项目正常工作, 需要做的工作.
October 03, 2016 - 18:26:11
Django version 1.10.1, using settings 'Project1.settings'
Starting development server at http://localhost:8000/
Quit the server with CTRL-BREAK.
[03/Oct/2016 18:26:38] "GET / HTTP/1.1" 200 1767
Not Found: /favicon.ico
[03/Oct/2016 18:26:38] "GET /favicon.ico HTTP/1.1" 404 1936
Not Found: /favicon.ico
[03/Oct/2016 18:26:38] "GET /favicon.ico HTTP/1.1" 404 1936

在浏览器输入     http://localhost:8000/

如果出现 It worked! 等信息, 表明成功运行了.

. 5. 写自己的views  . 修改 app1/views.py，添加以下内容:

  from django.http import HttpResponse

  def index(request):
      return HttpResponse("Hello world. This message is come from app1.views.index")

. 6. 创建urls.py 来定义该应用下面的url映射.  app1/urls.py, 内容如下:   (注意, 如果缺少了from . import views， 就会提示views对象找不到)

  from django.conf.urls import url

  from . import views

  urlpatterns = [
      url(r'^$', views.index, name = 'index'),
  ]  

  # https://docs.djangoproject.com/en/1.10/ref/urls/  关于 url 的官方文档

. 7. 下一步就是在root的url 映射中添加 app1/urls.py 来使该映射有效.  Project1/

  from django.conf.urls import include, url    # 注意，这儿增加了include 是为了把app1.urls 添加近来.

  from django.contrib import admin

  urlpatterns = [
      url(r'^app1/', include('app1.urls')),
      url(r'^admin/', admin.site.urls),
  ]   

. 8. 重新启动服务器, 并在浏览器访问

     manage.py runserver

     http://localhost:8000/app1/   -> 就是刚才编写的views.index 的内容

     http://localhost:8000/admin/  -> 弹出 登陆界面  , 实际用不了, 因为没有进行数据库相关的配置, 也没有进行登陆界面相关的配置.



----------------------------------------------------------

. 二、关于 Django的MTV模式

   Django的MTV模式 本质上和MVC是一样的，也是为了各组件间保持松耦合关系，只是定义上有些许不同，Django的MTV分别是值：

      M 代表模型（Model）：负责业务对象和数据库的关系映射(ORM)。

      T 代表模板 (Template)：负责如何把页面展示给用户(html)。

      V 代表视图（View）：负责业务逻辑，并在适当时候调用Model和Template。

   除了以上三层之外，还需要一个URL分发器，它的作用是将一个个URL的页面请求分发给不同的View处理，View再调用相应的Model和Template，MTV的响应模式如下所示：

. 三、 用户认证(初始配置)

  Django本身已经提供了用户认证模块，所以我们要做的事很简单，就是在它的基础上添加一些定制化的东西。默认情况下，Django的用户认证模块是打开的，可以通过以下步骤确认用户模块是否打开(在settings.py文件里)：

    1、确保 MIDDLEWARE_CLASSES 中包含 'django.contrib.sessions.middleware.SessionMiddleware'。

    2、确认 INSTALLED_APPS 中有 'django.contrib.sessions' 

    3、将 'django.contrib.auth' 放在你的 INSTALLED_APPS 设置中，然后运行 manage.py syncdb以创建对应的数据库表。

    4、确认 SessionMiddleware 后面的 MIDDLEWARE_CLASSES 设置中包含 'django.contrib.auth.middleware.AuthenticationMiddleware'。


  数据库配置

     用户认证系统必然离不开数据库，因为用户信息需要保存在数据库里，Django自带的用户认证系统也不例外。在使用它之前，必须配置数据库，Django支持大部分的主流数据库，这里我采用的是Oracle数据库，首先需要安装cx_Oracle模块，Django必须通过它才能访问Oracle数据库。至于如何安装cx_Oracle模块，这里就不讲了，具体查看官方文档。

    接着在Oracle中创建一个用户，我们Django项目创建的所有表都建在该用户下，因此需要相应的权限：

  -----------以下是MySQL  的部分 -----------

  http://blog.chinaunix.net/uid-29578485-id-5751415.html   新旧版本的命令变化。。。

  需要用户先装python-mysqldb   ---> Python 3 以后是 pymysql---> 还可以使用mysqlclient（不过用pip安装mysqlclient 的时候会出错.）

  1. 修改setting.py里面的DATABASES元组为

   DATABASES = {

      'default': {

          'ENGINE': 'django.db.backends.mysql', 

          'NAME': 'books',    #你的数据库名称

          'USER': 'root',   #你的数据库用户名

          'PASSWORD': '', #你的数据库密码

          'HOST': '', #你的数据库主机，留空默认为localhost

          'PORT': '3306', #你的数据库端口

      }

   }

   1.1 pymysql 与 mySQLdb 配置相同, 不需要改变。 最关键的是, 在Project/__init__.py 文件中, 添加如下代码:

   import pymysql
   
   pymysql.install_as_MySQLdb()

   2. INSTALLED_APPS = (                    # 这一步不加才能通过, 否则就会出错, 不知道是否是python3新版本的问题????

        'smms_db',#你的数据库名称

     )

   3. 在mysql里面创建books数据库

      create database smms_db;

   4. 检查配置是否有语法错误. 

      python manage.py validate

      1.10.1 版本命令修改为:  python manage.py check

(env2) F:\F_3_test\3_Python\adtest>manage.py check
System check identified no issues (0 silenced).

   5. 显示 mysql 语法    ####这一步也不支持

      python manage.py sqlall smms_db

   6. 同步模型库中的数据库   

      python manage.py syncdb

      这个命令没了。。。。用python manage.py help 看帮助.

      在Django 1.9及未来的版本种使用migrate代替syscdb.


   7. 下面开始创建 models ( 对应数据库表 )

      修改 app1/models.py , 添加下面的内容:

      import datetime
      from django.db import models

      from django.utils import timezone


      class Question(models.Model):
          question_text = models.CharField( max_length = 200 )
          pub_date = models.DateTimeField('date published')
          def __str__(self):
              return self.question_text

          def was_published_recently(self):
              return self.pub_date >= timezone.now() - datetime.timedelta( days = 1 )

      class Choice(models.Model):
          question = models.ForeignKey(Question, on_delete=models.CASCADE)
          choice_text = models.CharField(max_length=200)
          votes = models.IntegerField(default= 0)
          def __str__(self):
              return self.choice_text

      注意:

          __str__() 方法的定义非常重要, 不仅仅是一种交互式命令的约定俗成, 而且Django自动生成admin的时候用来展现对象内容也非常有用.

   8. 激活models

      上面的model代码提供给Django很多信息. 有了它,Django就可以完成以下工作：

      A. 为这个应用创建一个数据库schema（create table 语句）

      B. 通过访问Question 和Choice 对象，创建Python 数据库访问API

      但是, 首先,需要告诉 项目 app1 应用已经被安装了.  

      Django 应用是"pluggable"(插件化的), 你可以将一个应用在多个项目中使用, 也可以丢弃应用, 因为它们没有必须被捆绑到Django安装中.

      要在项目中包含应用app1, 需要在INSTALLED_APPS 设置中添加一个该应用配置的引用.  App1Config 类在 app1/apps.py 文件中.  所以引用路径是: 'app1.apps.App1Config'.  编辑Project1/settings.py文件,添加下面的点路径到INSTALL_APPS设置,如下:

      Project1/settings.py

      ---------------------------

          INSTALLED_APPS = [
              'app1.apps.App1Config',
              'django.contrib.admin',
              'django.contrib.auth',
              'django.contrib.contenttypes',
              'django.contrib.sessions',
              'django.contrib.messages',
              'django.contrib.staticfiles',
          ]

       ----------------------

      现在Django 知道包括app1应用了.运行另一个命令:

      (env2) F:\F_3_test\3_Python\Project1>manage.py makemigrations app1
      Migrations for 'app1':
        app1\migrations\0001_initial.py:
          - Create model Choice
          - Create model Question
          - Add field question to choice

      (env2) F:\F_3_test\3_Python\Project1>

       注意, 这一步不能少,如果没有这一步, ./migrations 子目录就没有0001_initial.py 文件, 后面的manage.py migrate 就会不真正处理该应用的models中数据库表的创建等.

------------------------

(env2) F:\F_3_test\3_Python\Project1>manage.py sqlmigrate app1 0001
BEGIN;
--
-- Create model Choice
--
CREATE TABLE `app1_choice` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `c
hoice_text` varchar(200) NOT NULL, `votes` integer NOT NULL);
--
-- Create model Question
--
CREATE TABLE `app1_question` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
`question_text` varchar(200) NOT NULL, `pub_date` datetime(6) NOT NULL);
--
-- Add field question to choice
--
ALTER TABLE `app1_choice` ADD COLUMN `question_id` integer NOT NULL;
ALTER TABLE `app1_choice` ALTER COLUMN `question_id` DROP DEFAULT;
CREATE INDEX `app1_choice_7aa0f6ee` ON `app1_choice` (`question_id`);
ALTER TABLE `app1_choice` ADD CONSTRAINT `app1_choice_question_id_67c40b2b_fk_ap
p1_question_id` FOREIGN KEY (`question_id`) REFERENCES `app1_question` (`id`);
COMMIT;

(env2) F:\F_3_test\3_Python\Project1>

===

数据库表列表

mysql> show tables;
+----------------------------+
| Tables_in_smms_db          |
+----------------------------+
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
| stockbaseinfotbl           |
+----------------------------+
11 rows in set (0.00 sec)


-----------------

(env2) F:\F_3_test\3_Python\Project1>manage.py migrate
Operations to perform:
  Apply all migrations: admin, app1, auth, contenttypes, sessions
Running migrations:
  Applying app1.0001_initial... OK

(env2) F:\F_3_test\3_Python\Project1>


mysql> show tables;
+----------------------------+
| Tables_in_smms_db          |
+----------------------------+
| app1_choice                |
| app1_question              |
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |a
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
| stockbaseinfotbl           |
+----------------------------+
13 rows in set (0.00 sec)

mysql>

可以发现增加了2张表: app1_choice, app1_question

http://blog.csdn.net/u011630575/article/details/51065052

##### 注意: 如果多个相同的相同应用名称 不同时间 创建并进行MTV操作, 由于数据库中的django_migrations 中已经有了 应用名称(app1)的0001_initial, 系统就判断没有数据发生变化, 不需要迁移, 结果就发生了如下问题:

(env2) F:\F_3_test\3_Python\project2>manage.py migrate
Operations to perform:
  Apply all migrations: admin, app1, auth, contenttypes, sessions
Running migrations:
  No migrations to apply.

### 删除数据库中的相关记录

mysql> delete from django_migrations where app='app1';
Query OK, 1 row affected (0.32 sec)

#### 再进行数据迁移更新, 就成功了. 新的数据库表也添加了.  不过不同的项目访问同一个数据库要非常小心, 防止出现冲突.

(env2) F:\F_3_test\3_Python\project2>manage.py migrate
Operations to perform:
  Apply all migrations: admin, app1, auth, contenttypes, sessions
Running migrations:
  Applying app1.0001_initial... OK

#####


如果又修改了 model.py 中相关库表对象的字段定义(增删字段等), 如果增加了字段要确认有缺省值,因为如果该表中的现有记录没有该字段的记录不会出错.

更新上面的修改只需要2个命令:

(env2) F:\F_3_test\3_Python\project2>manage.py makemigrations app1
Migrations for 'app1':
  app1\migrations\0002_choice2_testfield.py:
    - Add field testfield to choice2

(env2) F:\F_3_test\3_Python\project2>manage.py migrate
Operations to perform:
  Apply all migrations: admin, app1, auth, contenttypes, sessions
Running migrations:
  Applying app1.0002_choice2_testfield... OK

不在需要进行 manage.py sqlmigrate app1... 操作. 

====================================

总结:上面的数据操作其实就是3部分

  1. 修改models.py    应用下面的(比如: app1/models.py)添加模型(对应数据库表,如果没有，通过后面的操作可以创建数据库表)

  2. 修改配置文件Project/settings.py告诉项目应用可用了, 然后进行将应用进行迁移创建对应的model对象

     python manage.py makemigrations app1       (其实可以理解成装载应用app1, 这时候数据库其实没有任何变化) 

  3. 进行数据迁移同步, 将数据对象映射到数据库表中

     manage.py sqlmigrate app1 0001     (这个时候是解析应用app1的models，生成对应的sql 脚本, 其实并没有对数据库进行操作)

     manage.py migrate        ( 执行上面解析的sql脚本, 对数据库进行实际操作 )
 
     
  # 如果进行上面操作后, 又修改了models 中的字段定义, 那么第3步中的sqlmigrate 就不需要进行了, 其他步骤照常进行即可. 
======================manage.py 的shell 命令交互 参见第三讲 略 =================

. 关于 admin 用户管理

  1. 创建 一个admin用户

     python manage.py createsuperuser

     输入用户名/密码   admin/admin  , 还有个用来联系的email地址.

  2. 