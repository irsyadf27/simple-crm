from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    #email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    username = forms.EmailField(label = "Email")

    password1 = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=30, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=30, label="Confirm Password")
    organization_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )

