from django import forms
from .models import ImageUploadModel
<<<<<<< HEAD
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username', 'email','password']
=======
>>>>>>> bcde6757cd3e8f462d9e3530d628140754152c24

class UploadImageForm(forms.Form):
    title = forms.CharField(max_length=50)
    #file = forms.FileField()
    image = forms.ImageField()

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUploadModel
<<<<<<< HEAD
        fields = ('description', 'document' )
=======
        fields = ('description', 'document')
>>>>>>> bcde6757cd3e8f462d9e3530d628140754152c24
