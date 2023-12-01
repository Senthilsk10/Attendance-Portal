from django.urls import path
from .views import staffs,create_attendance_pool


urlpatterns = [
    path('profile/',staffs.as_view(),name = "staffs"),
    path('add_new_pool/',create_attendance_pool,name = "add_atendance_pool"),
]