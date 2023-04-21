from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


CLASSIFICATIONS = (
    ("Student", "I am a Student"),
    ("Teacher", "I am a Teacher"),
    ("Parent", "I am a Parent",),
)


class UserRegisterForm(UserCreationForm):
    '''This allows us to create a user'''
    email = forms.EmailField()
    classification = forms.ChoiceField(choices=CLASSIFICATIONS, required=True)

    class Meta:
        model = User
        fields = ['classification', 'username',
                  'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    '''This allows us to update the user'''
    email = forms.EmailField()
    classification = forms.ChoiceField(choices=CLASSIFICATIONS, required=True)

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    '''Allows us to update the image. It will look like it has combined with "UserUpdateForm" '''
    class Meta:
        model = Profile
        fields = ['image']
