from django.urls import path
from .views import UserLogin,welcome

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('welcome/',welcome.as_view(),name = "welcome")
]