from datetime import date

from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book

        fields = [
            "id",
            "title",
            "author",
            "description",
            "published_year",
            "price",
            "is_available",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]

    # Field-level validation
    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Title must contain at least 3 characters."
            )

        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Price cannot be negative."
            )

        return value

    def validate_published_year(self, value):
        current_year = date.today().year

        if value < 0:
            raise serializers.ValidationError(
                "Published year must be positive."
            )

        if value > current_year:
            raise serializers.ValidationError(
                "Published year cannot be in the future."
            )

        return value

    # Object-level validation
    def validate(self, attrs):
        author = attrs.get(
            "author",
            getattr(self.instance, "author", None)
        )

        is_available = attrs.get(
            "is_available",
            getattr(self.instance, "is_available", False)
        )

        if is_available and not author:
            raise serializers.ValidationError(
                "An available book must have an author."
            )

        return attrs