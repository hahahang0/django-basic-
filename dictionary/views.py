# from django.shortcuts import render

# # Create your views here.
# from rest_framework.views import APIView 
# from rest_framework.response import Response
# from rest_framework import mixins,generics

# # from dictionary.mixins import 

# from .models import Book 
# from .serializers import BookSerializer


# # class BookView(APIView):
# #     def get(self,request):
# #         self.say_hello()
# #         books = Book.objects.all()
# #         serializer = BookSerializer(
# #             books,
# #             many = True 
# #         )
# #         return Response(serializer.data)


# class BookListCreateView(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericAPIView
# ):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer 
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#     def post(self,request,*args,**kwargs):
#         return self.create(
#             request,*args,**kwargs
#         )

# class BookDetailView(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView,
# ):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(
#             request, *args, **kwargs
#         )

#     def put(self, request, *args, **kwargs):
#         return self.update(
#             request, *args, **kwargs
#         )

#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(
#             request, *args, **kwargs
#         )

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(
#             request, *args, **kwargs
#         )


####### FROM HERE WE ARE USING VIEWSET ######### 

# from requests import Session
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import action
from .pagination import BookLimitOffsetPagination, BookPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter
from rest_framework.filters import (SearchFilter,OrderingFilter)
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("id")
    serializer_class = BookSerializer
    # pagination_class = BookPagination
    pagination_class = BookLimitOffsetPagination

    ### customization 

    def perform_create(self,serializer):
        print("Create a new book.")
        serializer.save(
            owner = self.request.user
        )

    ### get_queryset() --> custom get query set 

    def get_queryset(self):
        # return Book.objects.filter(is_available=True)
        queryset = Book.objects.all()
        author = self.request.query_params.get("author")
        if author: 
            queryset = queryset.filter(
                author = author 
            )

        return queryset 
    
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    ]
    filterset_class = BookFilter
    search_fields = [
        "title",
        "author",
    ]
    ordering_fields = [
        "title",
        "price",
        "published_year",
        "created_at",
    ]

    authentication_classes=[
        # SessionAuthentication,
        # TokenAuthentication,
        JWTAuthentication,
    ]
    permission_classes=[
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]

        # filterset_fields = [
        #     "author",
        #     "published_year",
        #     "is_available",
        # ]

    ### we can also use custom action in ViewSet
    # if we want to return only available books
    @action(
        detail = False, 
        methods = ["get"]
    )

    # def who_am_i(self,request):
    #     return Response({
    #         "username" : request.user.username,
    #         "authenticated" : request.user.is_authenticated,
    #     })

    def available(self,request):
        books = Book.objects.filter(
            is_available = True
        )
        serializer = self.get_serializer(
            books,
            many=True
        )
        return Response(
            serializer.data
        )

    ########## AFTER THIS ..THE ROUTER AUTOMATICALLY CREATES GET /dictionary/books/available.


        # custom validation still belongs in the serializer . 