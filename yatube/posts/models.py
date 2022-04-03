from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    """ Модель для создания группы в соц.сети. """

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    # можно ли сделать так, чтобы была проверка
    # при создании поля на написания поля с большой
    # буквы (например, как метод capitalize в python для типа данных string?
    group_text = models.TextField()

    def __str__(self):
        return f'{self.title}'


class Post(models.Model):
    """ Модель для создания поста в соц.сети. """

    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='posts',
    )


class Event(models.Model):
    """Модель для создания событий в соц. сети. """

    name = models.CharField(max_length=200)
    start_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    contact = models.EmailField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='events'
    )
    location = models.CharField(max_length=400)
