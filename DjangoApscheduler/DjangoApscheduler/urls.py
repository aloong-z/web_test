"""DjangoApscheduler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from apptest.apscheduler import show_love, update

# from apscheduler.schedulers.background import BackgroundScheduler
# from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
#
# # 实例化调度器
# scheduler = BackgroundScheduler()
# # 调度器使用默认的DjangoJobStore()
# scheduler.add_jobstore(DjangoJobStore(), 'default')
#
#
# @register_job(scheduler, 'interval', id='test_show_love', seconds=5)
# def test():
#     # 具体要执行的代码
#     show_love()
#
#
# @register_job(scheduler, 'interval', id='test_update', seconds=18)
# def test_update():
#     # 具体要执行的代码
#     update()
#
#
# # 注册定时任务并开始
# register_events(scheduler)
# scheduler.start()


from apscheduler.schedulers.background import BackgroundScheduler


def test():
    # 具体要执行的代码
    show_love()


def test_update():
    # 具体要执行的代码
    update()


# 实例化调度器
scheduler = BackgroundScheduler()
scheduler.add_job(test, 'interval', seconds=5)
scheduler.add_job(test_update, 'interval', seconds=18)
# 注册定时任务并开始
scheduler.start()


urlpatterns = [
    path('admin/', admin.site.urls),
]
