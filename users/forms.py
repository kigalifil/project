from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from .models import Profile2


class UserRegistrationForm(UserCreationForm):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
    email = forms.EmailField()
    sex = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    Registration_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'max': datetime.now().date(), 'min': datetime.now().date()}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1, 'max': 150}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserUpdatedForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile2
        fields = ['image']
