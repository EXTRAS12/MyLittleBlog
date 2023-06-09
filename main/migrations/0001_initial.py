# Generated by Django 4.2.1 on 2023-06-07 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, verbose_name='Имя тэга')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Наименование')),
                ('slug', models.SlugField(blank=True, max_length=250, unique=True)),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/', verbose_name='Изображение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('views', models.IntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='main.tag')),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
                'ordering': ['-created_at'],
            },
        ),
    ]
