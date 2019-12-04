from django import forms
from users.models import User,UserProfile

class UserForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['matric_number','first_name','last_name','password','password_confirm']

        def clean(self):
            cleaned_data = super(UserForm, self).clean()
            pass_real = cleaned_data['password']
            pass_confirm = cleaned_data['password_confirm']
            if pass_real != pass_confirm:
                raise ValueError('password does not match ...lol')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['faculty','department']