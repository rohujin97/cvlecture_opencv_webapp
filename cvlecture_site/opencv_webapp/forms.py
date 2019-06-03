from django import forms
from .models import ImageUploadModel
from django.contrib.auth.models import User

# class UserForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['username', 'email', 'password']

class UploadImageForm(forms.Form):
    title = forms.CharField(max_length=50)
    #file = forms.FileField()
    image = forms.ImageField()

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUploadModel
        fields = ('description', 'document')
        fields = ('description', 'document')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(),
            'password': forms.PasswordInput(),
        }
