from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateField(auto_now=True)

class Client(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    updated_at = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)