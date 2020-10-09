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

class Event(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length = 50) #최대로 넣을 수 있는 글자 수
    description = models.TextField()

    def __str__(self): #제목에 오브젝트가 아니라 이름이 나오도록
        return self.name