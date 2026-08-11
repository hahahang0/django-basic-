from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

class BookPagination(PageNumberPagination):
    page_size=5
    page_size_query_param = "page_size"
    max_page_size = 50

class BookLimitOffsetPagination(
    LimitOffsetPagination
):
    default_limit = 15
    max_limit = 50

