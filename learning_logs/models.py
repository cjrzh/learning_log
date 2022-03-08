'''
Author: Mr. Zhangyi
Date: 2022-03-08 16:45:33
FilePath: /learning_log/learning_logs/models.py
Description: 
Copyright (c) 2022 by Mr. Zhangyi/Chinatelecom, All Rights Reserved. 
version: v0.1
'''
from django.db import models

# Create your models here.
class Topic(models.Model):
    """用户学习的主题。"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示。"""
        return self.text