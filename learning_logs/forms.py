'''
Author: Mr. Zhangyi
Date: 2022-03-09 16:13:57
FilePath: /learning_log/learning_logs/forms.py
Description: 
Copyright (c) 2022 by Mr. Zhangyi/Chinatelecom, All Rights Reserved. 
version: v0.1
'''
from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ' '}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
