from django.db import models
from django.contrib.auth.models import AbstractUser,User
from datetime import date

dept_choices = [
    ("IT", "Information Technology"),
    ("CSE", "Computer Science"),
    ("AI&ML", "Artificial Intelligence and Machine Learning")
]
role_choices = [
    ("Teacher", "Teacher"),
    ("Student", "Student")
]

request_choices = [
    ("late","late attendance"),
    ("leave","request leave")
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

sub_type_choices = [
    ("theory","Theory"),
    ("lab","Lab"),
    ("genral","genral"),
]

status_choices = [
    ("present","Present"),
    ("absent","Absent"),
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


class subject(models.Model):
    dept = models.CharField(max_length=45,choices=dept_choices,blank = False,null=False)
    sem = models.IntegerField(choices=sem_choices,blank = False,null=False)
    subject_name = models.CharField(max_length=45,blank=False,null=True)
    subject_code = models.CharField(max_length=10,blank=False,null=True,unique=True)
    type = models.CharField(max_length=45,choices=sub_type_choices,blank=False,null=True)

    def __str__(self):
        return self.subject_code

class attendance_pool(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(subject,on_delete=models.CASCADE)
    recieved_attendance = models.IntegerField(blank = True,null = False,default=0)
    is_alive = models.BooleanField(null=True,blank=False,default=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    datefield = models.DateTimeField(auto_now=True)


    
    def __str__(self):
        return f"{self.subject.subject_code} 's pool"
        pass

    def duration_display(self):
        return f"{self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"

class attendance(models.Model):
    pool = models.ForeignKey(attendance_pool,on_delete=models.CASCADE,blank=False,null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_roll = models.IntegerField(blank=False,null=False)
    status = models.CharField(max_length=20,choices=status_choices,default="absent",blank=False,null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pool}"

class request(models.Model):
    pool = models.ForeignKey(attendance_pool,on_delete=models.CASCADE,blank=False,null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_roll = models.IntegerField(blank=False,null=False)
    request_type = models.CharField(max_length=25,choices = request_choices,blank=False,null=False)