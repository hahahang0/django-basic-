# from django.urls import path 
# from .views import (BookListCreateView, BookDetailView)

# urlpatterns = [
#     path(
#         "dictionary/",
#         BookListCreateView.as_view(),
#         name='book-list-create'
#     ),
#     path(
#         'dictionary/<int:pk>/',
#         BookDetailView.as_view(),
#         name="book-detail"
#     )
# ]   

########### HERE STARTS THE ROUTER PART ############### 

from django.urls import path,include 
from rest_framework.routers import DefaultRouter 
from .views import BookViewSet

router = DefaultRouter()

router.register(
    "books",
    BookViewSet,
    basename='book'
)

urlpatterns = [
    path(
        "dictionary/",
        include(router.urls)
    ),
]