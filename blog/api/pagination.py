from rest_framework.pagination import PageNumberPagination



class MyCustomPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 's'
    max_page_size = 24
