from rest_framework import serializers
from .models import Book 
from datetime import date 

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Book 

        fields  = [
            "id",
            "title",
            "author",
            "description",
            "published_year",
            "price",
            "is_available",
            "created_at",
        ]

        read_only_field = [
            "id",
            "created_at",
        ]

        def validate_title(self,value):
            if len(value.strip()) < 3:
                raise serializers.ValidationError(
                    "Title must contain at least 3 characters."
                )
            return value

        def validate_price(self,value):
            if value < 0:
                raise serializers.ValidationError(
                    "Price cannot be negative."
                )
                
            return value;
        
        def validate_published_year(self,value):
            current_year = date.today().year
            if value<0:
                raise serializers.ValidationError(
                    "Published year must be positive."
                )
            if value>current_year:
                raise serializers.ValidationError(
                    "Published year cannot be in the future."
                )

            return value

# object level validation

        # def validate(self,attrs):
        #     author = attrs.get('author')
        #     is_available = attrs.get("is_available")

        #     if is_available and not author : 
        #         raise serializers.ValidationError(
        #             "An available book must have an author."
        #         )

        #     return attrs 
        def validate(self, attrs):

            if (
                attrs.get("is_available")
                and not attrs.get("author")
            ):

                raise serializers.ValidationError(
                    "An available book must have an author."
                )

            return attrs

# field validation --> one validation , object validation --> multiple validation