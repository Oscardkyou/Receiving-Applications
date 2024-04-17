from django import forms
from django.contrib.auth.models import User

from .models import Profile


class UserForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control stylish-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-control stylish-input'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'phone', 'company_name', 'birth_date', 'about']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'stylish-file', 'id': 'imageUpload', 'onchange': 'previewImage();'}),
            'phone': forms.TextInput(attrs={'class': 'form-control stylish-input'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control stylish-input'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control stylish-input', 'type': 'date'}),
            'about': forms.Textarea(attrs={'class': 'form-control stylish-textarea', 'rows': 3})
        }
