from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User



# Site About me page, appears as my dojo in navbar
class About(models.Model):
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
    

# User About me page, appears as my dojo in navbar
class AboutPage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s About Page"