from django.urls import path
from .views import *
from django_filters.views import FilterView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'courses'

urlpatterns = [
    path('verify_student_start/', verify_student_start,name='verify_student'),
    path('mycourses/', UserCoursesList,name='user_courses'),
    path('add/course/<int:pk>/add', add_course, name='add_course'),
    path('add/custom_course/', AddCustomCourseView.as_view(), name='add_course'),
    path('register/courses', RegisterCoursesList.as_view() ,name='register_courses'),
    

    path('search-up/', FilterView.as_view(filterset_class=UserFilter,
        template_name='register_course.html'), name='search'),
    
    path('<int:matric_number>/mycourses', UserCoursesList, name='user_detail'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)