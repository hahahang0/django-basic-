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

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import action
from .pagination import BookLimitOffsetPagination, BookPagination


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("id")
    serializer_class = BookSerializer
    # pagination_class = BookPagination
    pagination_class = BookLimitOffsetPagination

    ### customization 

    def perform_create(self,serializer):
        print("Create a new book.")
        serializer.save()

    ### get_queryset() --> custom get query set 

    def get_queryset(self):
        return Book.objects.filter(is_available=True)

    ### we can also use custom action in ViewSet
    # if we want to return only available books
    @action(
        detail = False, 
        methods = ["get"]
    )

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