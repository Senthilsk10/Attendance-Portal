from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from user.models import User,attendance_pool,subject,attendance
from django.views import View
from django.http import JsonResponse
import ipaddress
from django.utils import timezone
from datetime import timedelta


today = timezone.now().date()

this_week_start = today - timedelta(days=today.weekday())
this_week_end = this_week_start + timedelta(days=6)


class student(View):
    def get(self, request, *args, **kwargs):
        user_id = request.user.userid
        user_dept = request.user.dept
        user_sem = request.user.sem
        current_pools =attendance_pool.objects.filter(datefield__range=[this_week_start, this_week_end],subject__dept = user_dept,subject__sem = user_sem)
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
        userip = get_client_ip(request)
        id = request.POST.get('pool_id')
        user_pool = attendance_pool.objects.get(id = id)
        student = request.user
        student_rollno = student.userid
        attendance_status = "Present"

        attendance_data = attendance(
            pool = user_pool,
            user = student,
            student_roll = student_rollno,
            status = attendance_status,
            ip_address = userip
        )

        attendance_data.save()

        return JsonResponse("success",status = 200,safe=False)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # Ensure 'ip' is a valid IP address string
    try:
        ip_address = ipaddress.ip_address(ip)
    except ValueError:
        ip_address = None

    return str(ip_address)

from django.http import JsonResponse

def check_access(request):
    if request.method == "POST":
        user_ip = get_client_ip(request)
        user_id = request.user.userid
        pool_id = request.POST.get('pool_id')

        # Check if the user with the given user ID exists in the pool
        pool_userid_obj = attendance.objects.filter(pool__id=pool_id, user__userid=user_id).exists()

        # Check if the user with the given IP address exists in the pool
        pool_userip_obj = attendance.objects.filter(pool__id=pool_id, ip_address=user_ip).exists()

        # Define messages based on the conditions
        rollno_message = "flase" if pool_userid_obj else "true"
        ip_message = "false" if pool_userip_obj else "true"

        # Prepare the response data with messages
        data = {
            "roll_message": rollno_message,
            "ip_message": ip_message,
            "user_ip": user_ip,
        }

        return JsonResponse(data, status=200, safe=False)

        
def update_table_data(request):
    if request.method == "POST":
        pk = request.POST.get('pk')
        current_pool = attendance_pool.objects.get(id = pk)
        result_data = attendance.objects.filter(pool = current_pool)
        html_content = render_to_string('attendance_table_partial.html', {'result_data': result_data},request)

        return JsonResponse({'html_content': html_content})