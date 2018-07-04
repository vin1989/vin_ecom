from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from django.http import *
from django.contrib import auth
# Create your views here.
from .forms import *
from django.contrib.auth.models import User

def login(request):
    return render(request,'login1.html')


def index(request):
    return redirect('checkout')



def home(request):
    if request.user.is_authenticated():
        return index(request)
    else:
        return login(request)

def auth_view(request):
    #print request.POST,type(request)
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        
        return redirect('login_app:home')
    else:
        return HttpResponseRedirect('/invalid/')
    

def invalid_login(request):
    return render(request,'invalid_login.html')

def logout(request):
    auth.logout(request)
    #return render(request,'login.html')
    return redirect('login_app:home')

def signup(request):
    if request.method=='POST':
        form=Regforms(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password,
                                     email=email)
            return HttpResponseRedirect('/')
            #user = authenticate(username=username, password=password)
            #login(request, user)
            #return render(request,'login.html')
    else:
        form=Regforms()
    return render(request,'signup.html',{'form':form})




