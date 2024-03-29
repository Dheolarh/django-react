from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    authordp = models.ImageField(upload_to='media/images/', null=True, blank=True)
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    article = models.TextField()
    image = models.ImageField(upload_to='media/images/', null=True, blank=True)

    
    def __str__(self):
        return self.title
    