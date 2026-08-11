# class HelloMixin:
#     def say_hello(self):
#         print("Hello from the mixin!")

# from rest_framework.response import Response 


# class BookListMixin:
#     def list_books(self):
#         books = self.get_queryset()
#         serializer = self.get_serializer(
#             books,
#             many=True
#         )

#         return Response(
#             serializer.data
#         )

from rest_framework import mixins
 
class BookListCreateMixin(
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    pass