from django.db import models
from django.contrib.auth.models import User

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Добавьте другие поля вашего профиля

class Subscription(models.Model):
    subscriber = models.ForeignKey(User, related_name='subscriptions', on_delete=models.CASCADE)
    subscribed_to = models.ForeignKey(User, related_name='subscribers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE
    )
    nickname = models.CharField(max_length=55)
    description = models.TextField(null=True, blank=True)


class Post(models.Model):
    STATUS_CHOICES = (
        ('Posted', 'Posted'),
        ('Unposted', 'Unposted')
    )

    name = models.CharField('Header', max_length=80)
    description = models.TextField('Description', null=True)
    photo = models.ImageField('Photo', null=True, blank=True, upload_to="post_images/")
    status = models.CharField(
        'Status',
        max_length=200,
        choices=STATUS_CHOICES,
        default="Posted"
    )
    # M2O
    creator = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,  # необязательно в БД
        blank=False,  # обязательно в Django
        verbose_name="Автор поста",
        related_name="posts"  # default == post_set
    )

    category = models.ManyToManyField(
        to='Category',
        blank=True,
        verbose_name='Категории',
    )
    likes = models.IntegerField('Лайк', default=0)

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

    name = models.CharField(max_length=100, null=True, default='Default Category Name')
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.name} - {self.rating}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Comment(models.Model):
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE
    )
    comment_text = models.TextField()
    likes_qty = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True, blank=False
    )

    def __str__(self):
        return self.comment_text[:20]

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['created_at']

class Short(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField('Видео', upload_to='video_post/')
    created_at = models.DateTimeField(auto_now_add=True)
    # views = models.PositiveIntegerField(default=0)



    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return f'{self.video} - {self.created_at}'


class SavedPosts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.ManyToManyField(Post, verbose_name='saved post', related_name='saved_posts')

    class Meta:
        verbose_name = 'saved post'
        verbose_name_plural = 'saved posts'

    def __str__(self):
        return f'{self.user}'