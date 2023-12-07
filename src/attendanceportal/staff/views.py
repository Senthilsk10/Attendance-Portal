from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from user.models import attendance_pool,User,subject,attendance
from django.utils import timezone
from datetime import timedelta
from student.views import get_client_ip

# to calculate the recent data and past data for separate view
today = timezone.now().date()

this_week_start = today - timedelta(days=today.weekday())
this_week_end = this_week_start + timedelta(days=6)

this_month_start = today.replace(day=1)
this_month_end = (today.replace(day=1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)


class staffs(View):
    def get(self, request, *args, **kwargs):
        user_id = request.user.userid
        current_week_data = attendance_pool.objects.filter(datefield__range=[this_week_start, this_week_end],created_by=request.user)
        current_month_data = attendance_pool.objects.filter(datefield__range=[this_month_start, this_month_end],created_by=request.user)
        #pools = attendance_pool.objects.filter(created_by=request.user)
        template_name = "staffs.html"
        return render(request,template_name, {"user_id":user_id,"pools":current_week_data,"past_pools":current_month_data})


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

    subjects = subject.objects.filter(handling_staff = request.user)
    return render(request, 'add_attendance_pool.html',{"subjects":subjects})


class staffs_pool_view(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        current_pool = attendance_pool.objects.get(id = pk)
        result_data = attendance.objects.filter(pool = current_pool)
        template_name = "staff_pool_view.html"
        return render(request,template_name, {"this_week_pool":current_pool,"result_data":result_data})



 
