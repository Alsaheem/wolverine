from django.contrib import admin
from .models import Faculty,Semester,Level,UserCourses,Courses,Department
# Register your models here.

admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Level)
admin.site.register(Semester)
admin.site.register(Courses)
admin.site.register(UserCourses)

 