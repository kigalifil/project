from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post1(models.Model):
    Genre_CHOICES = (('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama', 'Drama'),('Horror','Horror'),('Western','Western'),('Romance','Romance'),('Adventure','Adventure'),('Music','Music'))
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='movies/')
    movie_length = models.CharField(max_length=50)
    movie_director = models.CharField(max_length=40)
    movie_actor = models.CharField(max_length=40)
    movie_url = models.URLField(max_length=100, null=True)
    movie_gne=models.CharField(choices=Genre_CHOICES,max_length=200,null=True)
    movie_likes=models.ManyToManyField(User,related_name='post_views')
    def total_likes(self):
        return self.movie_likes.count()


    def __str__(self):
        return f"{self.title}{self.content}{self.date_posted}{self.author}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    def snippet(self):
        return self.content[:10]+'.....'