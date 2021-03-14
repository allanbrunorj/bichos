from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='fotos_bichos')
    author = models.CharField(max_length=50)
    published_date = models.DateTimeField(blank=True, null=True)
    votes_up = models.IntegerField(default=0)
    votes_down = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title