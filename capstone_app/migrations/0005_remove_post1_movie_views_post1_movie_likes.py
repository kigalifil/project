# Generated by Django 4.0.6 on 2022-08-01 19:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('capstone_app', '0004_alter_post1_movie_gne'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post1',
            name='movie_views',
        ),
        migrations.AddField(
            model_name='post1',
            name='movie_likes',
            field=models.ManyToManyField(related_name='post_views', to=settings.AUTH_USER_MODEL),
        ),
    ]
