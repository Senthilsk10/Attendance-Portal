from django.shortcuts import render
from user.models import User,attendance_pool,subject
from django.views import View
# Create your views here.
class student(View):
    def get(self, request, *args, **kwargs):
        user_id = request.user.userid
        template_name = "student.html"
        return render(request,template_name, {"user_id":user_id})
