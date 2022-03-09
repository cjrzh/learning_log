'''
Author: Mr. Zhangyi
Date: 2022-03-08 16:45:33
FilePath: /learning_log/learning_logs/views.py
Description: 
Copyright (c) 2022 by Mr. Zhangyi/Chinatelecom, All Rights Reserved. 
version: v0.1
'''
from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """学习笔记的主页。"""
    return render(request, 'index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html',context)

def topic(request, topic_id):
    """显示单个主题及其所有的条目。"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'topic.html', context)