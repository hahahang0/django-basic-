from django.db import models
from django.conf import settings
from .managers import PostQuerySet
# Create your models here.

class Post(models.Model):
    objects = PostQuerySet.as_manager()
    
    title = models.CharField(
        max_length = 200
    )
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name ='posts'
    )
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    cover_image = models.ImageField(
        upload_to='post/',
        blank=True,
        null=True
    )
    attachment = models.FileField(
        upload_to = 'post_files/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title