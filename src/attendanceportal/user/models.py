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

sem_choices = [
    (1,"first semester"),
    (2,"second semester"),
    (3,"third semester"),
    (4,"fourth semester"),
    (5,"fifth semester"),
    (6,"sixth semester"),
    (7,"seventh semester"),
    (8,"eigth semester"),
]

class User(AbstractUser):
    dept = models.CharField(max_length=10, choices=dept_choices, blank=True, null=True)
    sem = models.IntegerField(choices = sem_choices,blank = True,null = True)
    role = models.CharField(max_length=10, choices=role_choices, default="Student", blank=False, null=False)
    userid = models.BigIntegerField(blank = False,null = False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['userid'], name='unique_user_id'),
        ]

