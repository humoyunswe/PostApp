from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone = forms.CharField(required=True,
    widget=forms.NumberInput(attrs={'placeholder': 'Enter the telefone number: '}),)
    data_of_birth = forms.DateField(
        required=True,
        widget=forms.DateInput(format='%d.%m.%Y',
        attrs={'placeholder': 'DD.MM.YYYY'}
    ),
    input_formats=['%d.%m.%Y']
    )

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'phone', 'data_of_birth', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    phone = forms.CharField()
    data_of_birth = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y'),
        input_formats=['%d.%m.%Y'], )
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
