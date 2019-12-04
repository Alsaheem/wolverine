from django.shortcuts import render
from .models import *

# Create your views here.
def UserCoursesList(request):
    user_courses =  UserCourses.objects.filter(user = request.user,semester__id= 1)
    return render(request,'user_courses_list.html',{'courses':user_courses})

# register courses list
def RegisterCourses(request,semester_id):
    # courses for the semester
    level = request.user.get_level()
    semester_courses = Courses.objects.filter(level=level,semester__id=semester_id)
    return render(request,'user_courses_list.html',{'courses':semester_courses})


def add_course(request,pk,**kwargs):
    if request.method == 'POST':
        semester = kwargs['semester']
        course_pick = Courses.objects.get(id=pk)
        # get_or_create
        user_courses = UserCourses.objects.get_or_create(user=request.user,semester=semester,level=level)
        add_course = user_courses.add(course_pick)
        add_course.save()


# get semester courses