from django.urls import path
from .views import student

urlpatterns = [
    path('profile/',student.as_view(),name = "student"),
]
