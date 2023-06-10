from time import time

from django.db import models
from django.urls import reverse
from pytils.translit import slugify

from account.models import User


def gen_slug(q):
    """Генератор слагов от времени"""
    new_slug = slugify(q)
    return new_slug + '-' + str(int(time()))


class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование')
    slug = models.SlugField(max_length=250, db_index=True, unique=True, blank=True)
    content = models.TextField(blank=True, verbose_name='Контент')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               max_length=100, blank=True, null=True, verbose_name='Имя автора')
    image = models.ImageField(upload_to='images/%Y/', verbose_name='Изображение', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Имя тэга')
    slug = models.SlugField(max_length=50, db_index=True, unique=True)
    description = models.TextField(default='')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title