from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    published_year = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='books'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return self.title;
    