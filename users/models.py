from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
import datetime as d
from courses.models import Faculty,Department
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save

def validate_matric_num(value):
    if len(str(value)) > 9 or len(str(value)) < 9 :
        raise ValidationError(
            _('%(value)s is not a valid registration/matric number'),
            params={'value': value},
        )

class UserManager(BaseUserManager):
    def create_user(self,matric_number,first_name,last_name,password=None):
        if not matric_number:
            raise ValueError('users must have a matric number')
        user = self.model(first_name=first_name,last_name=last_name,matric_number=matric_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,matric_number,first_name,last_name,password):
        user = self.create_user(matric_number,first_name,last_name,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    matric_number = models.IntegerField(unique=True,validators=[validate_matric_num],help_text='Please make sure your matric number is correct')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'matric_number'
    objects = UserManager()

    REQUIRED_FIELDS = ['first_name','last_name',]

    def get_enroll_year(self):
        matric = str(self.matric_number)
        year_entered = str(matric[:2])
        '''this function isnt really full fledged as it only gets the year within the 20's'''
        return '20'+year_entered

    def get_current_level_year(self):
        current_year = int(d.datetime.now().year)
        year_enrolled = int(self.get_enroll_year())
        '''this function isnt really full fledged because if the perso forfietes a semester , it isnt avvounted for'''
        level = current_year - year_enrolled
        return level

    def get_level(self):
        current_level = self.get_current_level_year()
        if current_level == 5:
            return '500'
        elif current_level == 4:
            return '400'
        elif current_level == 3:
            return '300'
        elif current_level == 2:
            return '200'
        elif current_level == 1:
            return '100'
        else:
            return 'Level Not Found Maybe Extra_year Student'


    def get_full_name(self):
        return '{} {}'.format(self.first_name,self.last_name)

    def __str__(self):
        return str(self.matric_number)

class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    head_shot = models.ImageField(upload_to='profile_images',blank=True)
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete = models.CASCADE)
    # user_image = models.ImageField(upload_to='')
    is_lecturer = models.BooleanField(default=False)

    def __str__(self):
        return '{}\s profile'.format(self.user.matric_number)


def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.get_or_create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)