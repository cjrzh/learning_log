'''
Author: Mr. Zhangyi
Date: 2022-03-08 16:45:33
FilePath: /learning_log/learning_logs/views.py
Description: 
Copyright (c) 2022 by Mr. Zhangyi/Chinatelecom, All Rights Reserved. 
version: v0.1
'''
from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm

# Create your views here.


def index(request):
    """学习笔记的主页。"""
    return render(request, 'index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)


def topic(request, topic_id):
    """显示单个主题及其所有的条目。"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'topic.html', context)


def new_topic(request):
    if request.method != 'POST':
        # 未提交数据：创建一个新表单。
        form = TopicForm()
    else:    # POST提交的数据：对数据进行处理。
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    # 显示空表单或指出表单数据无效。
    context = {'form': form}
    return render(request, 'new_topic.html', context)


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'new_entry.html', context)
