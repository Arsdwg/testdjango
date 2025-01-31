# Generated by Django 5.0.6 on 2024-06-01 12:17

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('author', models.CharField(max_length=100, verbose_name='Бренд')),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='Укажите фото')),
                ('descript', models.TextField(verbose_name='Описание')),
                ('music', models.FileField(blank=True, upload_to='audio/', verbose_name='Аудио озвучка')),
                ('video', models.URLField(blank=True, verbose_name='Укажите ссылку на видео')),
                ('category', models.CharField(choices=[('бу', 'бу'), ('новое', 'новое')], max_length=100, verbose_name='Категория')),
                ('review', models.TextField(verbose_name='Отзыв специалиста')),
                ('pages', models.PositiveIntegerField(verbose_name='Год выпуска')),
                ('time_book', models.PositiveIntegerField(verbose_name='укажите время новости')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'добавить предмет',
                'verbose_name_plural': 'список предметов',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.PositiveIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('text', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('what', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_item', to='items.postitem')),
            ],
        ),
    ]
