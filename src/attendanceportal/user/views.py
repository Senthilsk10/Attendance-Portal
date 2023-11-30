from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse
from .models import User,attendance_pool,subject
# Create your views here.


class UserLogin(LoginView):
    success_url = reverse_lazy("welcome")

class welcome(View):
    def get(self, request, *args, **kwargs):
        user_role = request.user.role
        if(user_role == "Student"):
            return redirect('student')
        else:
            return redirect('staffs')

class student(View):
    def get(self, request, *args, **kwargs):
        user_id = request.user.userid
        template_name = "student.html"
        return render(request,template_name, {"user_id":user_id})


class staffs(View):
    def get(self, request, *args, **kwargs):
        user_id = request.user.userid
        pools = attendance_pool.objects.filter(created_by=request.user)
        #poolid = pool.id
        template_name = "staffs.html"
        return render(request,template_name, {"user_id":user_id,"pools":pools})
    

class Base_view(View):
    def get(self,request):
        template_name = 'welcome.html'
        return render(request,template_name)


def create_attendance_pool(request):
    if request.method == 'POST':
        # Retrieve data from the submitted form
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        sub_id = int(request.POST.get('subject'))
        sub_obj = subject.objects.get(id=sub_id)
        #received_attendance = request.POST.get('received_attendance')
        is_alive = request.POST.get('is_alive') == 'on'  # Convert checkbox value to boolean
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))
        created_by_id = request.POST.get('created_by')
        # You can also get other fields similarly

        # Create a new instance of the attendance_pool model
        attendance_instance = attendance_pool(
            start_time=start_time,
            end_time=end_time,
            subject = sub_obj,
            #received_attendance=received_attendance,
            is_alive=is_alive,
            latitude=latitude,
            longitude=longitude,
            created_by_id=created_by_id,
            # Set other fields accordingly
        )

        # Save the instance to the database
        attendance_instance.save()

        return redirect('staffs')  # Redirect to a success page or another URL

    subjects = subject.objects.all()
    return render(request, 'add_attendance_pool.html',{"subjects":subjects})