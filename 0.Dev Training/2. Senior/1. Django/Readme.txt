. �μ�:

   https://www.djangoproject.com/download/

   http://blog.csdn.net/column/details/djangonote.html

   https://docs.djangoproject.com/en/1.10/intro/tutorial01/

. 1. ��װ Django

     pip install Django==1.10.1

. 2. ���� Django ��Ŀ

     �������Ӧ�Ŀ����������ٴ�����Ŀ, �Ժ�������.

     django-admin.py startproject Project1    

     Project1 ����Ŀ����. ���������ᴴ��Project1Ŀ¼�Լ��������һЩ��Ŀ¼���ļ�.

(env2) F:\F_3_test\3_Python>cd Project1

(env2) F:\F_3_test\3_Python\Project1>dir
 ������ F �еľ��� �ĵ�
 ������к��� 000E-B5CB

 F:\F_3_test\3_Python\Project1 ��Ŀ¼

2016/10/03  18:23    <DIR>          .
2016/10/03  18:23    <DIR>          ..
2016/10/03  18:23    <DIR>          Project1
2016/10/03  18:23               804 manage.py
               1 ���ļ�            804 �ֽ�
               3 ��Ŀ¼ 133,223,604,224 �����ֽ�


. 3. ����Ӧ��

     ������ĿĿ¼  Project1, ����

(env2) F:\F_3_test\3_Python\Project1>manage.py startapp app1

(env2) F:\F_3_test\3_Python\Project1>dir
 ������ F �еľ��� �ĵ�
 ������к��� 000E-B5CB

 F:\F_3_test\3_Python\Project1 ��Ŀ¼

2016/10/03  18:25    <DIR>          .
2016/10/03  18:25    <DIR>          ..
2016/10/03  18:25    <DIR>          Project1
2016/10/03  18:25    <DIR>          app1
2016/10/03  18:23               804 manage.py
               1 ���ļ�            804 �ֽ�
               4 ��Ŀ¼ 133,223,596,032 �����ֽ�

. 4. ����֮ǰ�Ĳ����Ƿ�ɹ�.

(env2) F:\F_3_test\3_Python\Project1>manage.py runserver localhost:8000
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you
 apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.  ---------------------------------------> �����ʾ�����Ҫ��Ŀ��������, ��Ҫ���Ĺ���.
October 03, 2016 - 18:26:11
Django version 1.10.1, using settings 'Project1.settings'
Starting development server at http://localhost:8000/
Quit the server with CTRL-BREAK.
[03/Oct/2016 18:26:38] "GET / HTTP/1.1" 200 1767
Not Found: /favicon.ico
[03/Oct/2016 18:26:38] "GET /favicon.ico HTTP/1.1" 404 1936
Not Found: /favicon.ico
[03/Oct/2016 18:26:38] "GET /favicon.ico HTTP/1.1" 404 1936

�����������     http://localhost:8000/

������� It worked! ����Ϣ, �����ɹ�������.

. 5. д�Լ���views  . �޸� app1/views.py�������������:

  from django.http import HttpResponse

  def index(request):
      return HttpResponse("Hello world. This message is come from app1.views.index")

. 6. ����urls.py �������Ӧ�������urlӳ��.  app1/urls.py, ��������:   (ע��, ���ȱ����from . import views�� �ͻ���ʾviews�����Ҳ���)

  from django.conf.urls import url

  from . import views

  urlpatterns = [
      url(r'^$', views.index, name = 'index'),
  ]  

  # https://docs.djangoproject.com/en/1.10/ref/urls/  ���� url �Ĺٷ��ĵ�

. 7. ��һ��������root��url ӳ������� app1/urls.py ��ʹ��ӳ����Ч.  Project1/

  from django.conf.urls import include, url    # ע�⣬���������include ��Ϊ�˰�app1.urls ��ӽ���.

  from django.contrib import admin

  urlpatterns = [
      url(r'^app1/', include('app1.urls')),
      url(r'^admin/', admin.site.urls),
  ]   

. 8. ��������������, �������������

     manage.py runserver

     http://localhost:8000/app1/   -> ���Ǹղű�д��views.index ������

     http://localhost:8000/admin/  -> ���� ��½����  , ʵ���ò���, ��Ϊû�н������ݿ���ص�����, Ҳû�н��е�½������ص�����.



----------------------------------------------------------

. �������� Django��MTVģʽ

   Django��MTVģʽ �����Ϻ�MVC��һ���ģ�Ҳ��Ϊ�˸�����䱣������Ϲ�ϵ��ֻ�Ƕ�������Щ��ͬ��Django��MTV�ֱ���ֵ��

      M ����ģ�ͣ�Model��������ҵ���������ݿ�Ĺ�ϵӳ��(ORM)��

      T ����ģ�� (Template)��������ΰ�ҳ��չʾ���û�(html)��

      V ������ͼ��View��������ҵ���߼��������ʵ�ʱ�����Model��Template��

   ������������֮�⣬����Ҫһ��URL�ַ��������������ǽ�һ����URL��ҳ������ַ�����ͬ��View����View�ٵ�����Ӧ��Model��Template��MTV����Ӧģʽ������ʾ��

. ���� �û���֤(��ʼ����)

  Django�����Ѿ��ṩ���û���֤ģ�飬��������Ҫ�����ºܼ򵥣����������Ļ��������һЩ���ƻ��Ķ�����Ĭ������£�Django���û���֤ģ���Ǵ򿪵ģ�����ͨ�����²���ȷ���û�ģ���Ƿ��(��settings.py�ļ���)��

    1��ȷ�� MIDDLEWARE_CLASSES �а��� 'django.contrib.sessions.middleware.SessionMiddleware'��

    2��ȷ�� INSTALLED_APPS ���� 'django.contrib.sessions' 

    3���� 'django.contrib.auth' ������� INSTALLED_APPS �����У�Ȼ������ manage.py syncdb�Դ�����Ӧ�����ݿ��

    4��ȷ�� SessionMiddleware ����� MIDDLEWARE_CLASSES �����а��� 'django.contrib.auth.middleware.AuthenticationMiddleware'��


  ���ݿ�����

     �û���֤ϵͳ��Ȼ�벻�����ݿ⣬��Ϊ�û���Ϣ��Ҫ���������ݿ��Django�Դ����û���֤ϵͳҲ�����⡣��ʹ����֮ǰ�������������ݿ⣬Django֧�ִ󲿷ֵ��������ݿ⣬�����Ҳ��õ���Oracle���ݿ⣬������Ҫ��װcx_Oracleģ�飬Django����ͨ�������ܷ���Oracle���ݿ⡣������ΰ�װcx_Oracleģ�飬����Ͳ����ˣ�����鿴�ٷ��ĵ���

    ������Oracle�д���һ���û�������Django��Ŀ���������б����ڸ��û��£������Ҫ��Ӧ��Ȩ�ޣ�

  -----------������MySQL  �Ĳ��� -----------

  http://blog.chinaunix.net/uid-29578485-id-5751415.html   �¾ɰ汾������仯������

  ��Ҫ�û���װpython-mysqldb   ---> Python 3 �Ժ��� pymysql---> ������ʹ��mysqlclient��������pip��װmysqlclient ��ʱ������.��

  1. �޸�setting.py�����DATABASESԪ��Ϊ

   DATABASES = {

      'default': {

          'ENGINE': 'django.db.backends.mysql', 

          'NAME': 'books',    #������ݿ�����

          'USER': 'root',   #������ݿ��û���

          'PASSWORD': '', #������ݿ�����

          'HOST': '', #������ݿ�����������Ĭ��Ϊlocalhost

          'PORT': '3306', #������ݿ�˿�

      }

   }

   1.1 pymysql �� mySQLdb ������ͬ, ����Ҫ�ı䡣 ��ؼ�����, ��Project/__init__.py �ļ���, ������´���:

   import pymysql
   
   pymysql.install_as_MySQLdb()

   2. INSTALLED_APPS = (                    # ��һ�����Ӳ���ͨ��, ����ͻ����, ��֪���Ƿ���python3�°汾������????

        'smms_db',#������ݿ�����

     )

   3. ��mysql���洴��books���ݿ�

      create database smms_db;

   4. ��������Ƿ����﷨����. 

      python manage.py validate

      1.10.1 �汾�����޸�Ϊ:  python manage.py check

(env2) F:\F_3_test\3_Python\adtest>manage.py check
System check identified no issues (0 silenced).

   5. ��ʾ mysql �﷨    ####��һ��Ҳ��֧��

      python manage.py sqlall smms_db

   6. ͬ��ģ�Ϳ��е����ݿ�   

      python manage.py syncdb

      �������û�ˡ���������python manage.py help ������.

      ��Django 1.9��δ���İ汾��ʹ��migrate����syscdb.


   7. ���濪ʼ���� models ( ��Ӧ���ݿ�� )

      �޸� app1/models.py , ������������:

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

      ע��:

          __str__() �����Ķ���ǳ���Ҫ, ��������һ�ֽ���ʽ�����Լ���׳�, ����Django�Զ�����admin��ʱ������չ�ֶ�������Ҳ�ǳ�����.

   8. ����models

      �����model�����ṩ��Django�ܶ���Ϣ. ������,Django�Ϳ���������¹�����

      A. Ϊ���Ӧ�ô���һ�����ݿ�schema��create table ��䣩

      B. ͨ������Question ��Choice ���󣬴���Python ���ݿ����API

      ����, ����,��Ҫ���� ��Ŀ app1 Ӧ���Ѿ�����װ��.  

      Django Ӧ����"pluggable"(�������), ����Խ�һ��Ӧ���ڶ����Ŀ��ʹ��, Ҳ���Զ���Ӧ��, ��Ϊ����û�б��뱻����Django��װ��.

      Ҫ����Ŀ�а���Ӧ��app1, ��Ҫ��INSTALLED_APPS ���������һ����Ӧ�����õ�����.  App1Config ���� app1/apps.py �ļ���.  ��������·����: 'app1.apps.App1Config'.  �༭Project1/settings.py�ļ�,�������ĵ�·����INSTALL_APPS����,����:

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

      ����Django ֪������app1Ӧ����.������һ������:

      (env2) F:\F_3_test\3_Python\Project1>manage.py makemigrations app1
      Migrations for 'app1':
        app1\migrations\0001_initial.py:
          - Create model Choice
          - Create model Question
          - Add field question to choice

      (env2) F:\F_3_test\3_Python\Project1>

       ע��, ��һ��������,���û����һ��, ./migrations ��Ŀ¼��û��0001_initial.py �ļ�, �����manage.py migrate �ͻ᲻���������Ӧ�õ�models�����ݿ��Ĵ�����.

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

���ݿ���б�

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

���Է���������2�ű�: app1_choice, app1_question

http://blog.csdn.net/u011630575/article/details/51065052

##### ע��: ��������ͬ����ͬӦ������ ��ͬʱ�� ����������MTV����, �������ݿ��е�django_migrations ���Ѿ����� Ӧ������(app1)��0001_initial, ϵͳ���ж�û�����ݷ����仯, ����ҪǨ��, ����ͷ�������������:

(env2) F:\F_3_test\3_Python\project2>manage.py migrate
Operations to perform:
  Apply all migrations: admin, app1, auth, contenttypes, sessions
Running migrations:
  No migrations to apply.

### ɾ�����ݿ��е���ؼ�¼

mysql> delete from django_migrations where app='app1';
Query OK, 1 row affected (0.32 sec)

#### �ٽ�������Ǩ�Ƹ���, �ͳɹ���. �µ����ݿ��Ҳ�����.  ������ͬ����Ŀ����ͬһ�����ݿ�Ҫ�ǳ�С��, ��ֹ���ֳ�ͻ.

(env2) F:\F_3_test\3_Python\project2>manage.py migrate
Operations to perform:
  Apply all migrations: admin, app1, auth, contenttypes, sessions
Running migrations:
  Applying app1.0001_initial... OK

#####


������޸��� model.py ����ؿ�������ֶζ���(��ɾ�ֶε�), ����������ֶ�Ҫȷ����ȱʡֵ,��Ϊ����ñ��е����м�¼û�и��ֶεļ�¼�������.

����������޸�ֻ��Ҫ2������:

(env2) F:\F_3_test\3_Python\project2>manage.py makemigrations app1
Migrations for 'app1':
  app1\migrations\0002_choice2_testfield.py:
    - Add field testfield to choice2

(env2) F:\F_3_test\3_Python\project2>manage.py migrate
Operations to perform:
  Apply all migrations: admin, app1, auth, contenttypes, sessions
Running migrations:
  Applying app1.0002_choice2_testfield... OK

������Ҫ���� manage.py sqlmigrate app1... ����. 

====================================

�ܽ�:��������ݲ�����ʵ����3����

  1. �޸�models.py    Ӧ�������(����: app1/models.py)���ģ��(��Ӧ���ݿ��,���û�У�ͨ������Ĳ������Դ������ݿ��)

  2. �޸������ļ�Project/settings.py������ĿӦ�ÿ�����, Ȼ����н�Ӧ�ý���Ǩ�ƴ�����Ӧ��model����

     python manage.py makemigrations app1       (��ʵ��������װ��Ӧ��app1, ��ʱ�����ݿ���ʵû���κα仯) 

  3. ��������Ǩ��ͬ��, �����ݶ���ӳ�䵽���ݿ����

     manage.py sqlmigrate app1 0001     (���ʱ���ǽ���Ӧ��app1��models�����ɶ�Ӧ��sql �ű�, ��ʵ��û�ж����ݿ���в���)

     manage.py migrate        ( ִ�����������sql�ű�, �����ݿ����ʵ�ʲ��� )
 
     
  # ����������������, ���޸���models �е��ֶζ���, ��ô��3���е�sqlmigrate �Ͳ���Ҫ������, ���������ճ����м���. 
======================manage.py ��shell ����� �μ������� �� =================

. ���� admin �û�����

  1. ���� һ��admin�û�

     python manage.py createsuperuser

     �����û���/����   admin/admin  , ���и�������ϵ��email��ַ.

  2. 