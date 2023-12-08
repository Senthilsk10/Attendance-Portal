from django.urls import path
from .views import staffs,create_attendance_pool,staffs_pool_view,get_requests


urlpatterns = [
    path('profile/',staffs.as_view(),name = "staffs"),
    path('add_new_pool/',create_attendance_pool,name = "add_atendance_pool"),
    path('view/pool/<int:pk>/',staffs_pool_view.as_view(),name = "staffs_pool_view"),
    path("get_requests/<int:pk>/",get_requests,name = "get_requests"),
]