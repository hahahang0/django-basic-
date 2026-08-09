from django.urls import path
from . import views

urlpatterns = [
      path('',views.home,name='amazon-home'),
      path("products/<int:id>/",views.product_details),
      path("products/product_list/",views.product_list,name="product-list"),
      path("products/create/",views.create_product,name="create_product"),
      path("products/<int:id>/edit/",views.update_product,name="update_product")
]