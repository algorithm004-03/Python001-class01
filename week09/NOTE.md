第九周学习笔记

Django管理页面

1、迁移生成表 

$ python manage.py makemigrations

$ python manage.py migrate

2、创建管理员账号

$ python manage.py createsuperuser

3、增加自定义的模型： 

./index/admin.py

from .models import Type, Name 

# 注册模型 

admin.site.register(Type) 

admin.site.register(Name)

二、Form、Auth 组件，实现用户登录和密码验证功能

1、创建文件

#form.py 

from django import forms 

class LoginForm(forms.Form): 

username = forms.CharField() 

password = forms.CharField(widget=forms.PasswordInput, min_length=6)


2、views.py中定义函数

三、celery定时任务的实现

1. Redis 

安装和启动 

2. 安装

Celery 

pip install celery 

pip install redis==3.5.3

pip install celery-with-redis 

pip install django-celery

3. 添加app

django-admin startproject MyDjango 

python manager.py startapp djcron

INSTALL_APPS=[ 
'djcelery', 
'djcron' 
]

4. 迁移生成表 

python manage.py makemigrations

python manage.py migrate

5. 配置django时区 

from celery.schedules import crontab 

from celery.schedules import timedelta 

import djcelery 

djcelery.setup_loader() 

BROKER_URL = 'redis://:123456@127.0.0.1:6379/'  # 代理人 

CELERY_IMPORTS = ('djcron.tasks')  # app 

CELERY_TIMEZONE = 'Asia/Shanghai' # 时区 

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler' # 定时任务调度器

6. 在MyDjango下建立celery.py 

import os from celery import Celery, platforms 

from django.conf import settings 

os.environ.setdefault('DJANGO_SETTINGS_MODULE','MyDjango.settings') 

app = Celery('MyDjango') 

app.config_from_object('django.conf:settings') 

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS) 

platforms.C_FORCE_ROOT = True

在__init__.py 增加

# 使用绝对引入，后续使用import引入会忽略当前目录下的包 

from __future__ import absolute_import 

from .celery import app as celery_app

from MyDjango.celery import app

@app.task() 
def task1(): 
    return 'test1'

@app.task() 
def task2(): 
    return 'test2'



启动Celery 

celery -A MyDjango beat -l info 

celery -A MyDjango worker -l info
