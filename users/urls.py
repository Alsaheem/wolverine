from django.urls import path
from .views import register
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    # path('', UserCoursesList,name='user_courses'),
    path('register/', register ,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('login/',auth_views.LogoutView.as_view(template_name='registration/logout.html')),
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    
]