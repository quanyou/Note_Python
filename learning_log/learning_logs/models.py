# from django.db import models
#
#
# # Create your models here.
#
# class Topic(models.Model):
#
#     """topic of user's study’"""
#     text = models.CharField(max_length=200)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self): # please user __unicode__ instead of __str__ in Python2.7
#         """return the describe of model's string"""
#         return self.text
#
#
# class Entry(models.Model):
#
#     """学到的有关某个主题的具体知识"""
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE())
#     text = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#
#
#     class Meta:
#
#         verbose_name_plural = 'entries'
#
#     def __str__(self):
#
#         """return model's string"""
#         return self.text[:50] + "..."


# _*_ coding: utf-8 _*_
