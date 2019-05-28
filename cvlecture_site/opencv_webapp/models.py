from django.db import models

# Create your models here.
<<<<<<< HEAD

#class ImageUploadModel(models.Model):
#    description = models.CharField(max_length=255, blank=True)
#    document = models.ImageField(upload_to='images/%Y/%m/%d')
#    uploaded_at = models.DateTimeField(auto_now_add=True)

class ImageUploadModel(models.Model):
  description = models.CharField(max_length=255, blank=True)
  document = models.ImageField(upload_to='images/%Y/%m/%d')
  uploaded_at = models.DateTimeField(auto_now_add=True)
=======
class ImageUploadModel(models.Model):
  description = models.CharField(max_length=255, blank=True)
  document = models.ImageField(upload_to='images/%Y/%m/%d')
  uploaded_at = models.DateTimeField(auto_now_add=True)
>>>>>>> bcde6757cd3e8f462d9e3530d628140754152c24
