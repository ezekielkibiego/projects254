from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=50)
    image = CloudinaryField("image", null=True)
    description = models.TextField(max_length=600)
    techs_used = models.TextField(max_length=100, null=True)
    url = models.URLField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def __str__(self):
        return self.title