from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'personal/home.html')

def index(request):
   return render (request,'personal/home.html')

def contact(request):
    return render (request,'personal/basic.html',{'content': ['If you would like to contact me, please email me','rupanisantosh@gmail.com']} )


