from django.urls import path
from .views import register
from django.contrib.auth import views as auth_views
from .views import HomeView,DashboardView,about
app_name = 'users'

urlpatterns = [
    path('', HomeView.as_view() ,name='home'),
    path('dashboard/', DashboardView.as_view() ,name='dashboard'),
    path('register/', register ,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html')),
    path('about/',about,name='about'),
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    
]