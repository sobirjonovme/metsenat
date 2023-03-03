from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from students.models import University, Student
from students.api.serializers import UniversitySerializer, StudentSerializer, StudentDetailSerializer
from common.pagination import DefaultPagination


# UNIVERSITY VIEWS
class UniversityListAPIView(ListCreateAPIView):
    queryset = University.objects.all().order_by('name')
    serializer_class = UniversitySerializer

    permission_classes = [IsAuthenticated]


class UniversityDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

    permission_classes = [IsAuthenticated]


# STUDENT VIEWS
class StudentListAPIView(ListCreateAPIView):
    queryset = Student.objects.all().order_by('-created_at')
    serializer_class = StudentSerializer
    pagination_class = DefaultPagination
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = {
            'type': ['exact'],
            'university': ['exact'],
        }
    search_fields = ['full_name', 'phone_number']


class StudentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer

    permission_classes = [IsAuthenticated]
