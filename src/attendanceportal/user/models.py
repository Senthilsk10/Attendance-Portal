from django.db import models
from django.contrib.auth.models import AbstractUser

dept_choices = [
    ("IT", "Information Technology"),
    ("CSE", "Computer Science"),
    ("AI&ML", "Artificial Intelligence and Machine Learning")
]
role_choices = [
    ("Teacher", "Teacher"),
    ("Student", "Student")
]

class User(AbstractUser):
    dept = models.CharField(max_length=10, choices=dept_choices, blank=True, null=True)
    role = models.CharField(max_length=10, choices=role_choices, default="Student", blank=False, null=False)
    userid = models.BigIntegerField(blank = False,null = False)