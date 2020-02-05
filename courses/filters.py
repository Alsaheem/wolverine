import django_filters
from .models import Courses
from django import forms





class UserFilter(django_filters.FilterSet):
    course_code = django_filters.CharFilter(lookup_expr='icontains')
    name = django_filters.CharFilter(lookup_expr='icontains')
 

    class Meta:
        model = Courses
        fields = ['name', 'name']



# class UserFilter(django_filters.FilterSet):
#     class Meta:
#         model = Courses
#         fields = {
#             'course_code': ['icontains', ],
#             'name': ['icontains', ],

#         }