from django.shortcuts import render
from user.models import User,attendance_pool,subject
from django.views import View
# Create your views here.
class student(View):
    def get(self, request, *args, **kwargs):
        user_id = request.user.userid
        user_dept = request.user.dept
        user_sem = request.user.sem
        current_pools =attendance_pool.objects.filter(subject__dept = user_dept,subject__sem = user_sem)
        template_name = "student.html"
        return render(request,template_name, {"user_id":user_id,"pools":current_pools})

class pool_view(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        current_pool = attendance_pool.objects.get(id = pk)
        template_name = "student_pool_view.html"
        return render(request,template_name, {"pool":current_pool})


