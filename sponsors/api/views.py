from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from sponsors.models import Sponsor
from sponsors.api.serializers import RegisterSponsorSerializer, SponsorSerializer
from common.pagination import DefaultPagination


class RegisterSponsorAPIView(CreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = RegisterSponsorSerializer


class SponsorListAPIView(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    pagination_class = DefaultPagination
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = {
            'status': ['exact'],
            'total_money': ['exact'],
            'created_at': ['gte', 'lte'],
        }
    search_fields = ['full_name', 'phone_number']


class SponsorDetailAPIView(RetrieveUpdateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

    permission_classes = [IsAuthenticated]
