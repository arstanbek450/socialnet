from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user =  models.OneToOneField(
        to=User,
        on_delete=models.CASCADE
    )
    nickname = models.CharField(max_length=55)
    description = models.TextField(null=True, blank=True)

class Post(models.Model):
    STATUS_CHOICES = (
        ('Опубликован', 'Опубликован'),
        ('Не опубликован', 'Не опубликован'),
    )

    name = models.CharField(max_length=80)
    description = models.TextField()
    photo = models.ImageField(upload_to='post_photos/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    rating = models.IntegerField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
