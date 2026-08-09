from django.contrib import admin

# Register your models here.
from .models import Category,Product,Customer,Order,OrderItem
# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields=("name",)
# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "name",
        "price",
        "stock",
        "category",
        "inventory_status",
    )
    def inventory_status(self,obj): #this is kind of a helper function in django.
        if obj.stock > 10: 
            return "In stock"
        elif obj.stock <= 5 and obj.stock > 0:
            return "Low stock"
        else: 
            return "out of stock"
    
    

    list_filter=(
        "stock",
        )
    search_fields=(
        "category",
    )
    ordering=(
        "-price",
    )
    list_editable=(
        "price",
        "stock",
    )
    readonly_fields=(
        "created_at",
        "updated_at",
        "deleted_at",
    )
    fieldsets = (

    (
        "Basic Information",
        {
            "fields": (
                "name",
                "category",
            )
        },
    ),

    (
        "Inventory",
        {
            "fields": (
                "price",
                "stock",
            )
        },
    ),

    # 

    )
    date_hierarchy = 'created_at'

    autocomplete_fields = (
        "category",
    )
    
class OrderItemInline(admin.TabularInline):
    model = OrderItem 
    extra = 1 

# class CustomerInline(admin.TabularInline):
#     model = Customer
#     extra = 1 


# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     inlines = [
#         CustomerInline
#     ]

admin.site.register(Customer)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines= [
        OrderItemInline
    ]
# admin.site.register(Order)
admin.site.register(OrderItem)