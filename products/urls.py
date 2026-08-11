from django.urls import path 
from .views import  ProductListCreateView,ProductDetailView

urlpatterns  = [
    path(
        'products/',
        ProductListCreateView.as_view(),
        name="product-list-create"
    ),
    # path(
    #     'products/create/',ProductCreateView.as_view(),name="product-create"
    # ),
    path(
        'product/<int:pk>/',ProductDetailView.as_view(),name='product-detail'
    )
]