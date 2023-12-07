from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from user.models import attendance_pool,User,subject
# Create your views here.

class staffs(View):
    def get(self, request, *args, **kwargs):
        user_id = request.user.userid
        pools = attendance_pool.objects.filter(created_by=request.user)
        #poolid = pool.id
        template_name = "staffs.html"
        return render(request,template_name, {"user_id":user_id,"pools":pools})


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