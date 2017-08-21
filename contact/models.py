#coding: utf-8
from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return "message from {name}".format(name=self.name)