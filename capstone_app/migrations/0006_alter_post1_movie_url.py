# Generated by Django 4.1 on 2022-08-06 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone_app', '0005_remove_post1_movie_views_post1_movie_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post1',
            name='movie_url',
            field=models.URLField(max_length=100, null=True),
        ),
    ]
