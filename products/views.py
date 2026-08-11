from django.shortcuts import render

# Create your views here.
from rest_framework.generics import (ListCreateAPIView,ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView)
from .models import Product 
from .serializers import ProductSerializer


# class ProductListView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# real world example 

# class ProductListView(ListAPIView):
#     serializer_class = ProductSerializer
#     # for filtering ...
#     # def get_queryset(self):
#     #     queryset = Product.objects.all()
#     #     available = self.request.query_params.get("available")
#     #     if available == "true":
#     #         queryset = queryset.filter(is_available=True)
#     #     return queryset

#     # for searching ... 
#     def get_queryset(self):
#         queryset = Product.objects.all()

#         search = self.request.query_params.get("search")
        
#         min_price = self.request.query_params.get("min_price")
#         max_price = self.request.query_params.get('max_price')
#         if search:
#             queryset = queryset.filter(name__icontains=search)
#         if min_price : 
#             queryset = queryset.filter(price__gte = min_price)
#         if max_price : 
#             queryset = queryset.filter(price_lte = max_price)
#         return queryset;
    

# class ProductCreateView(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # def perform_create(self,serializer): # this function is used for further customization.
#     #     serializer.save()

class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer;

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class=  ProductSerializer 
    def perform_update(self,serializer):
        serializer.save(updated_by=self.request.user)

