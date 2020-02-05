from django.shortcuts import render,redirect
from .models import Faculty,Courses,Semester,Level,Department,UserCourses
from .models import Semester,Level
from django.contrib.auth.decorators import login_required
from django.views import View
from .face_dec import face_dect
from users.models import User,UserProfile
from django.views.generic import TemplateView, ListView
from .filters import UserFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

@login_required()

def UserCoursesList(request, matric_number):
    user = User.objects.get(matric_number=matric_number)
    user_courses =  UserCourses.objects.filter(user = user).order_by('level')
    return render(request,'user_courses_list.html',{'courses':user_courses,'user':user})

# # register courses list
class RegisterCoursesList(View):

    def get(self,request):
        # courses for the semester
        user_level = int(request.user.get_level())
        real_level = Level.objects.get(name=user_level)
        print(real_level)
        semester = Semester.objects.get(active=True)
        semester_courses = Courses.objects.filter(level=real_level,semester=semester)
        print(semester_courses)
        return render(request,'register_current_semester.html',{'courses':semester_courses})

    def post():
        pass

# Add Custom Course
class AddCustomCourseView(View):

    def get(self,request):
        return render(request,'add_custom_course.html',{})

    def post():
        pass

def add_course(request,pk,**kwargs):
    user_level = int(request.user.get_level())
    real_level = Level.objects.get(name=user_level)
    course_pick = Courses.objects.get(pk=pk)
    print(course_pick)
    course_semester = course_pick.semester
    user_courses = UserCourses.objects.get(user=request.user,semester=course_semester,level=real_level)
    add_course = user_courses.courses.add(course_pick)
    print('course has been added')
    return redirect('courses:register_courses')


def remove_course(request,pk,**kwargs):
    user_level = int(request.user.get_level())
    real_level = Level.objects.get(name=user_level)
    course_pick = Courses.objects.get(pk=pk)
    print(course_pick)
    course_semester = course_pick.semester
    user_courses = UserCourses.objects.get(user=request.user,semester=course_semester,level=real_level)
    add_course = user_courses.courses.remove(course_pick)
    # add_course.save()
    print('course has been removed')
    return redirect('courses:register_courses')

def search(request):
    user_list = Courses.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'register_courses.html', {'filter': user_filter})


class SearchResultsView(ListView):
    model = Courses
    template_name = 'search_courses.html'

    def get(self,request):
    # courses for the semester
        user_level = int(request.user.get_level())
        real_level = Level.objects.get(name=user_level)
        print(real_level)
        semester = Semester.objects.get(active=True)
        semester_courses = Courses.objects.filter(level=real_level,semester=semester)
        print(semester_courses)
        return render(request,'search_courses.html',{'courses':semester_courses})

# add and delete courses
def verify_student_start(request):
    if request.method == 'GET':
        return render(request,'verify_student.html',{})
    if request.method=='POST':
        matric_number = int(request.POST.get('matric_number'))
        if request.user.is_staff == True:
            student = User.objects.get(matric_number=matric_number)
            student_profile = UserProfile.objects.get(user=student)
            student_picture_url = student_profile.head_shot.url
            if student is not None:
                full_url = 'C:/Users/VECTOR/Desktop/wolverine/' + student_picture_url
                face_dect(full_url)
                if True:
                    print('redirecting to the dashboard now')
                    return redirect('courses:user_detail',matric_number=matric_number)
                # else:
                #     return redirect('courses:home')
                #     pass
            else:
                return redirect('courses:home')
                pass
        else:
            return redirect('courses:home')

    