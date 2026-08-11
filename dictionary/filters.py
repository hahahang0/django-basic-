import django_filters 
from .models import Book 

class BookFilter(django_filters.FilterSet):
    # there are kind of like custom filters ... filtering machinery
    title = django_filters.CharFilter(
        field_name = 'title',
        lookup_expr = 'icontains'
    )
    author = django_filters.CharFilter(
        field_name='author',
        lookup_expr = 'icontains'
    )
    min_price = django_filters.NumberFilter(

        field_name = 'price',
        lookup_expr = 'gte'
    )
    max_price = django_filters.NumberFilter(
        field_name = 'price',
        lookup_expr = 'lte'
    )
    class Meta:
        model = Book 
        fields = [ # this is auto-filtering ... here django auto-filters this fields 
            "author",
            "published_year",
            "is_available"
        ]