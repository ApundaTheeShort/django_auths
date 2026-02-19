from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm as BaseUserChangeForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('phone_number', 'email', 'first_name', 'last_name')


class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('phone_number', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')


class CustomLoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())
