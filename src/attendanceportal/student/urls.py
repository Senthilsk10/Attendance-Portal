from django.urls import path
from .views import student,pool_view,get_attendance,check_access,update_table_data,get_request,checkpoint_request

urlpatterns = [
    path('profile/',student.as_view(),name = "student"),
    path('view/pool/<int:pk>/',pool_view.as_view(),name = "student_pool_view"),
    path("markPresence/",get_attendance,name = "mark_presence"),
    path("check_access/",check_access,name = "check_access"),
    path("refreshData/",update_table_data,name = "GetTableData"),
    path("save_request/<int:pk>/",get_request,name = "save_request"),
    path("check_access_for_request/<int:pk>/",checkpoint_request,name = "checkpoint_request")
]
