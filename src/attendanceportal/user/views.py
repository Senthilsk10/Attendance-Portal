from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse
# Create your views here.


class UserLogin(LoginView):
    success_url = reverse_lazy("welcome")

class welcome(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")
    
class Base_view(View):
    def get(self,request):
        template_name = 'base.html'
        return render(request,template_name)