from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Группы'
        verbose_name = 'Группа'

    def __str__(self):
        return self.title


class Post(models.Model):

    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE,
        related_name='posts', blank=True, null=True
    )

    class Meta:
        ordering = ('pub_date',)

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )

    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name='Подписан',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'following'),
                name='unique_following'
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F('following')),
                name='following'
            )
        ]

    def __str__(self):
        return (
            f'Подписчик: {self.user.username}, автор {self.following.username}'
        )
