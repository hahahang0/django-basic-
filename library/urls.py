from django.urls import path 
# from . import views 
from .views import BookListView,BookDetailView

urlpatterns = [
    # path("",views.home)
    path(
        "books/",
        BookListView.as_view(),
        name='book-list'
    ),
    path(
        "books/<int:pk>",
        BookDetailView.as_view(),
        name="book-detail"
    ),
]