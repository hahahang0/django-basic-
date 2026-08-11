from .models import Book 
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = [
            "id",
            "title",
            "author",
            "price",
            "published_year",
            "is_available",
        ]
        read_only_fields=[
            "id"
        ]