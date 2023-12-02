from django.shortcuts import render,redirect
from user.models import User,attendance_pool,subject,attendance
from django.views import View
from django.http import JsonResponse
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
        result_data = attendance.objects.filter(pool = current_pool)
        template_name = "student_pool_view.html"
        return render(request,template_name, {"pool":current_pool,"result_data":result_data})


def get_attendance(request):#exception arises as anonymous user userid doesnot exists so handle it
    if request.method == 'POST':
        id = request.POST.get('pool_id')
        user_pool = attendance_pool.objects.get(id = id)
        student = request.user
        student_rollno = student.userid
        attendance_status = "Present"

        attendance_data = attendance(
            pool = user_pool,
            user = student,
            student_roll = student_rollno,
            status = attendance_status
        )

        attendance_data.save()

        return JsonResponse("success",status = 200,safe=False)
