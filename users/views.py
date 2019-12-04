from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect,HttpResponse
from .models import User,UserProfile
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm,UserProfileForm
from django.views.generic import View,TemplateView
from django.contrib import messages 

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

# get user courses
def UserProfileView(request):
    pass


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
    



