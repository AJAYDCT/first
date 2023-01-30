from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.
def index(request):
    contex_dict ={'text':'Hi bro','number':200}
    return render(request,'tempapp/index.html',contex_dict)

def other(request):
    return render(request,'tempapp/other.html')

def relative(request):
    return render(request,'tempapp/relative_url_templates.html')

def Login(request):
    if request.user.is_authenticated:
        return render(request,"index.html")
    else:
        messages.info(request,"Please login bro!")
        return HttpResponseRedirect('/')

def LoginUser(request):
    if request.method == "POST":
        username= request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username= username, password = password)
        if user != None:
            login(request,user)
            return HttpResponseRedirect('/tempapp')
        else:
            messages.error(request, "Enter data correctly")
            return HttpResponseRedirect('/')

def LogoutUser(request):
    logout(request)
    request.user =- None
    return HttpResponseRedirect('/')

