from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
import json


class Task(models.Model):
    TASK_TYPE = [
        ('1', 'Test'),
        ('2', 'Text')
    ]
    
    number = models.PositiveIntegerField()
    theme = models.CharField(max_length=30)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=2000, blank=True)
    type = models.CharField(max_length=1, choices=TASK_TYPE)
    answer = models.JSONField()

    def __str__(self) -> str:
        return f'{self.number}: {self.name} \n {self.description}'
    
    def ret_answer(self):
        return self.answer


class Logik(AbstractUser):
    tasks = models.ManyToManyField(Task, through='LogikTask')
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']


u_logik = get_user_model()

class LogikTask(models.Model):
    SOLVED = [
        ('0', 'No'),
        ('1', 'Yes'),
        ('2', 'None')
    ]
    logik = models.ForeignKey(u_logik, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    accept_date = models.DateTimeField()
    answer = models.JSONField(default=dict)
    solved = models.CharField(max_length=1, choices=SOLVED)
