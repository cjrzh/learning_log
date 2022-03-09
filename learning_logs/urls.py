'''
Author: Mr. Zhangyi
Date: 2022-03-09 09:55:00
FilePath: /learning_log/learning_logs/urls.py
Description: 定义learning_logs的URL模式。
Copyright (c) 2022 by Mr. Zhangyi/Chinatelecom, All Rights Reserved. 
version: v0.1
'''
from django.urls import path
from . import views
app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
