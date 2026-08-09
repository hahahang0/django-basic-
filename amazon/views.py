from email.header import Header
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Product,Category, ProductManager
# Create your views here.
def home(request):
    return render(request,'amazon/home.html')

# def product_details(request,id):
#     # product = Product.objects.get(id=id)
#     product = get_object_or_404(
#         Product, 
#         id = id 
#     )
#     return HttpResponse(
#         # f"Your requested product {id}"
#         f"""
#         Product : {product.name}
#         Product : {product.price}
#         Product : {product.stock}

#         """

#     )

def product_details(request,id):
    product = get_object_or_404(
        Product,
        id = id
    )

    return render(
        request,
        "amazon/product_details.html",
        {
            "product" : product
        }
        
    )

def product_list(request):
    search = request.GET.get(
        "search"
    )

    products = Product.objects.available()
    if search:
        products = products.filter(
            name__icontains=search
        )

    return render(
        request,
        "amazon/product_list.html",
        {
            "products" : products,
            "search" : search,
        }
    )


def create_product(request):
    if request.method == "POST":
        name = request.POST.get(
            "name"
        )
        price = request.POST.get(
            "price"
        )
        stock = request.POST.get(
            "stock"
        )
        category_id = request.POST.get(
            "category"
        )
        Product.objects.create(
            name = name ,
            price = price, 
            stock  = stock,
            category_id = category_id,
        )
        # return HttpResponse(
        #     "Product Created !"
        # )
        return redirect(
            "product-list"
        )

    categories = Category.objects.all()

    return render(
            request,"amazon/create_product.html",
            {
                "categories" : categories
            }
        )

# def edit_product()
def update_product(request,id):
    product = get_object_or_404(
        Product,
        id=id
    )
    categories = Category.objects.all()
    if request.method == "POST":
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.stock = request.POST.get("stock")
        product.category_id = request.POST.get("category_id")
        # print("CATEGORY:", product.category_id)

        product.save()
        
        return redirect("product-list")

    return render(
        request,
        "amazon/update_product.html",
        {
            "product" : product,
            "categories" : categories,
        }

    )

def delete_product(request,id):
    product = get_object_or_404(
        Product,
        id = id 
    )
    if request.method == "POST":
        product.delete()
        return redirect("product-list")

    return render(
        request,
        "amazon/delete_product.html",
        {
            "product":product,
        }
    )

