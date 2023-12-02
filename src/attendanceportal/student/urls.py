from django.urls import path
from .views import student,pool_view

urlpatterns = [
    path('profile/',student.as_view(),name = "student"),
    path('view/pool/<int:pk>/',pool_view.as_view(),name = "student_pool_view")
]
