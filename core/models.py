# Short с полями user, video (file_field), дата содания, количество просмотров
# SavedPosts, с полем user (O2O), post (M2M)
# В Posts добавьте likes (positive interger, default=0)
# Все модели отобразить в админке и добавить по 3 записи
from django.db import models
from django.contrib.auth.models import User

class SavedPosts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    posts = models.ManyToManyField(to='Post',
                                   verbose_name='Saved Post',
                                   related_name='saved_posts')

    class Meta:
        verbose_name = 'Сохраненные видео'
        verbose_name_plural = 'Сохраненные видео'
class Shorts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to='video/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return f'{self.video} - {self.created_at}'
class Profile(models.Model):
    user = models.OneToOneField(
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
    creator = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        verbose_name="Автор поста",
        related_name="posts"
    )
    # content = models.TextField()
    likes = models.PositiveIntegerField('likes', default=0)

    def __str__(self):
        return f'{self.name} - {self.status}'

    category = models.ManyToManyField(
        to='Category',
        blank=True,
        verbose_name='Категории')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.name} - {self.status}'



class Category(models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10)
    )
    name = models.CharField('Наименование столбца', max_length=50)
    rating = models.PositiveSmallIntegerField('Рейтинг', choices=RATING_CHOICES, null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name} - {self.rating}'

class Comment(models.Model):
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
    )
    comment_text = models.TextField()
    likes_qty = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text[:20]

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"
        ordering = ['created_at']