from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAuthenticatedOrReadOnly

from .models import Post 
from .serailizers import PostSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.views import APIView
from django.core.cache import cache
from rest_framework.response import Response

# Create your views here.

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all().order_by("-created_at")
#     # queryset = Post.objects.published()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     def perform_create(self, serializer):
#         # return super().perform_create(serializer)
#         serializer.save(
#             author=self.request.user
#         )



class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer 
    def get_queryset(self):
        queryset = Post.objects.all()
        if not self.request.user.is_staff:
            queryset = queryset.published()
        return queryset 
    def perform_create(self,serializer):
        serializer.save(
            author = self.request.user
        )


class BlogStatsView(APIView):
    def get(self,request):
        count = cache.get("published-post-count")
        if count is None:
            count = Post.objects.published().count()
            cache.set("published-post-count",count,300)
        return Response({
            "published_posts" : count
        })