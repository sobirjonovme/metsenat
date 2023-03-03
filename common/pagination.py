from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DefaultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': super().get_next_link(),
                'previous': super().get_previous_link()
            },
            'total_elements': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'page_size': self.get_page_size(self.request),
            'page': super().get_page_number(self.request, self.page.paginator),
            'results': data
        })
