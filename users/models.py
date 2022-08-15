from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone


# Create your models here.

class Profile2(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super(Profile2, self).save(*args, **kwargs)
        img = Image.open(self.image.name)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.name)


class Movies(models.Model):
    name = models.CharField(max_length=200)
    discriptions = models.TextField(max_length=20000)
    image = models.ImageField(upload_to='movies/')
    movie_length = models.CharField(max_length=50)
    released_date = models.DateTimeField(default=timezone.now)
    movie_director = models.CharField(max_length=40)
    movie_actor = models.CharField(max_length=40)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.image}'
