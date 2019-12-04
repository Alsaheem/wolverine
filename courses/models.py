from django.db import models
from django.conf import settings

# Create your models here.

class Faculty(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length = 100)
    faculty = models.ForeignKey(Faculty,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Semester(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Courses(models.Model):
    name = models.CharField(max_length = 100)
    course_code = models.CharField(max_length=6)
    level = models.ForeignKey(Level,on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    semester = models.ForeignKey(Semester,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class UserCourses(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE)
    level = models.ForeignKey(Level,on_delete=models.DO_NOTHING)
    courses = models.ManyToManyField(Courses)

    class Meta:
        ordering = ['-level']

    def __str__(self):
        return '{}--{} level--{} semester'.format(str(self.user.matric_number),self.level,self.semester)
