# Generated by Django 5.1.6 on 2025-02-14 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0002_category_donation_remove_book_author_post_like_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='donation',
            options={'verbose_name': 'Донат', 'verbose_name_plural': 'Донаты'},
        ),
        migrations.AlterModelOptions(
            name='like',
            options={'verbose_name': 'Лайк', 'verbose_name_plural': 'Лайки'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Публикация', 'verbose_name_plural': 'Публикации'},
        ),
    ]
