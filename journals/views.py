from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAuthenticatedOrReadOnly

from .models import Post 
from .serailizers import PostSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.object().all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        # return super().perform_create(serializer)
        serializer.save(
            author=self.request.user
        )
