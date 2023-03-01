from django.urls import path

from students.api.views import (
    UniversityListAPIView, UniversityDetailAPIView,
    StudentListAPIView, StudentDetailAPIView
)


app_name = 'students'

urlpatterns = [
    path('', StudentListAPIView.as_view(), name='student-list'),
    path('<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),

    path('universities/', UniversityListAPIView.as_view(), name='university-list'),
    path('universities/<int:pk>/', UniversityDetailAPIView.as_view(), name='university-detail'),
]
