from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(
        max_length=200
    )
    author = models.CharField(
        max_length=100
    )
    description = models.TextField(
        blank=True
    )
    published_year = models.IntegerField()
    price = models.DecimalField(
        max_digits = 10,
        decimal_places=2
    )
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title 