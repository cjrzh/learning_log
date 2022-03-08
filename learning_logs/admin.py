'''
Author: Mr. Zhangyi
Date: 2022-03-08 16:45:33
FilePath: /learning_log/learning_logs/admin.py
Description: 
Copyright (c) 2022 by Mr. Zhangyi/Chinatelecom, All Rights Reserved. 
version: v0.1
'''
from django.contrib import admin

# Register your models here.
from .models import Topic
admin.site.register(Topic)
