from django.db import models

from django.contrib.auth.models import User


class ProfileUserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    first_name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/user.png')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"