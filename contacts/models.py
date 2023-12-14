from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20, null=False)
    email = models.EmailField()
    notes = models.TextField(max_length=200, default="")
    created_time = models.TimeField(auto_now=False, auto_now_add=False)
