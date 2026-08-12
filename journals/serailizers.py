from rest_framework import serializers
from .models import Post 

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = [
            "id",
            "title",
            "content",
            "author",
            'cover_image',
            'attachment',
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "author",
            "created_at",
            "updated_at",
        ]

    def validate_cover_image(self,image):
        if image.size > 5 * 1024 * 1024:
            raise serializers.ValidationError(
                "Image must be smaller than 5 MB"
            )
        return image