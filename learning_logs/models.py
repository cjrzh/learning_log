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

class Entry(models.Model):
    """学到的有关某个主题的具体知识。"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'entries'
        def __str__(self):
            """返回模型的字符串表示。"""
            return f"{self.text[:50]}..."