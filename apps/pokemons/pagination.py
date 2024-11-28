from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPokemonPagination(PageNumberPagination):
    page_size = 20  # Tamaño de la página (20 registros por página)
    page_size_query_param = 'page_size'  # Permitir ajustar el tamaño con ?page_size=

    def get_paginated_response(self, data):
        return Response({
            'current_page': self.page.number,
            'total_pages': self.page.paginator.num_pages,
            'total_items': self.page.paginator.count,
            'has_next': self.page.has_next(),
            'has_previous': self.page.has_previous(),
            'results': data
        })
