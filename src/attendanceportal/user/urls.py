from django.urls import path
from .views import UserLogin,welcome,staffs,student,create_attendance_pool

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('welcome/',welcome.as_view(),name = "welcome"),
    path('student/',student.as_view(),name = "student"),
    path('staff/',staffs.as_view(),name = "staffs"),
    path('add_new_pool',create_attendance_pool,name = "add_atendance_pool"),
]