from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect,HttpResponse
from .models import User,UserProfile
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm,UserProfileForm,LoginForm
from django.views.generic import View,TemplateView
from django.contrib import messages 
from django.urls import path, include

# import face_recognition
# import cv2 

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

class HomeView(TemplateView):
    template_name='home.html'

# register user
def register(request):
    Registered = False
    user_form = UserForm()
    profile_form = UserProfileForm()
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST)
        user_form = UserForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            Registered = True
        else:
            print(user_form.errors,profile_form.errors)
    return render(request,'registration/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':Registered})
 

def about(request):
    return render(request,"about.html",{})

