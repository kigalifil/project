# Generated by Django 4.0.6 on 2022-07-28 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post1',
            name='movie_url',
            field=models.FileField(null=True, upload_to='movies_url/'),
        ),
    ]
