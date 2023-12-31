from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse,JsonResponse
from user.models import attendance_pool,User,subject,attendance,attendance_request
from django.utils import timezone
from datetime import timedelta
from student.views import get_client_ip
from django.template.loader import render_to_string
from django.db.models import Q

# to calculate the recent data and past data for separate view
today = timezone.now().date()

this_week_start = today - timedelta(days=today.weekday())
this_week_end = this_week_start + timedelta(days=6)

class staffs(View):
    def get(self, request, *args, **kwargs):
        user_id = request.user.userid
        current_week_data = attendance_pool.objects.filter(datefield__range=[this_week_start, this_week_end],created_by=request.user).exclude(datefield=today)
        today_pools = attendance_pool.objects.filter(datefield=today)
        
        template_name = "staffs.html"
        return render(request,template_name, {"user_id":user_id,"week_pools":current_week_data,"pools":today_pools})


def create_attendance_pool(request):
    if request.method == 'POST':
        
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        sub_id = int(request.POST.get('subject'))
        sub_obj = subject.objects.get(id=sub_id)
        #received_attendance = request.POST.get('received_attendance')
        is_alive = request.POST.get('is_alive') == 'on'  # Convert checkbox value to boolean
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))
        created_by_id = request.POST.get('created_by')
        
        attendance_instance = attendance_pool(
            start_time=start_time,
            end_time=end_time,
            subject = sub_obj,
            #received_attendance=received_attendance,
            is_alive=is_alive,
            latitude=latitude,
            longitude=longitude,
            created_by_id=created_by_id,
            
        )

        
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
        return render(request,template_name, {"pool":current_pool,"result_data":result_data})


def get_requests(request,*args,**kwargs):
    if request.method == "GET":
        pk = kwargs.get('pk')
        result_data = attendance_request.objects.filter(pool = pk)
        html_content = render_to_string('requests_objects_partial.html', {'requests': result_data},request)

        return JsonResponse({'html_content': html_content})
    else:
        return JsonResponse("post requests not allowed",status = 400)
 

def post_attendance(request,*args,**kwargs):
    if request.method == "GET":
        default_ip = "10.0.0.0"
        pk = kwargs.get("pk")
        request_obj = attendance_request.objects.get(id =pk)
        student = request_obj.user
        attendance_status = request_obj.request_type
        user_pool = request_obj.pool

        attendance_data = attendance(
            pool = user_pool,
            user = student,
            student_roll = student.userid,
            status = attendance_status,
            ip_address = default_ip
        )

        attendance_data.save()
        request_obj.delete()
        data = {
            "message":"added successfully"
        }
        return JsonResponse(data, status=200)


def delete_requests(request,*args,**kwargs):
    if request.method == "POST":
        pk = kwargs.get("pk")
        request_obj = attendance_request.objects.get(id=pk)
        request_obj.delete()
        data = {
            "message":"deleted successfully successfully"
        }
        return JsonResponse(data, status=200)


def turn_off(request,*args,**kwargs):
    if request.method == "GET":
        pk = kwargs.get("pk")
        pool = attendance_pool.objects.get(id = pk)
        pool.is_alive = False
        pool.save()
        return redirect("staffs_pool_view",pk = pk)

def turn_on(request,*args,**kwargs):
    if request.method == "GET":
        pk = kwargs.get("pk")
        pool = attendance_pool.objects.get(id = pk)
        pool.is_alive = True
        pool.save()
        return redirect("staffs_pool_view",pk = pk)


def search_pools(request,*args,**kwargs):
    if request.method == "GET":
        date = request.GET.get("search")
        text = request.GET.get('text')
        if date is not None and text is not None:
            result_pools = attendance_pool.objects.filter(Q(datefield=date) | Q(subject__subject_name=text),created_by = request.user)
            html_content = render_to_string('pools_partial.html', {'pools': result_pools},request)
        else:
            html_content = render_to_string('no_search.html',{'message':"not a valid request"},request)
        return JsonResponse({'html_content': html_content})
    else:
        return JsonResponse("post requests not allowed",status = 400)