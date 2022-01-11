from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class Task(models.Model):
    content = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    task_list = models.ForeignKey(List, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content