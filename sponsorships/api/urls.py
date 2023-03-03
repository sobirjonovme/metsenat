from django.urls import path

from sponsorships.api.views import (
    SponsorStudentCreateAPIView, SponsorStudentDetailAPIView,
    OverallStatistics, SponsorStatistics, StudentStatistics
)


app_name = 'sponsorships'

urlpatterns = [
    path('create/', SponsorStudentCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', SponsorStudentDetailAPIView.as_view(), name='detail'),

    path('dashboard/overall-statistics/', OverallStatistics.as_view(), name='dashboard-overall'),
    path('dashboard/sponsors/', SponsorStatistics.as_view(), name='dashboard-sponsors'),
    path('dashboard/students/', StudentStatistics.as_view(), name='dashboard-students'),
]
