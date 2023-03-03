from django.urls import path

from sponsorships.api.views import SponsorStudentCreateAPIView, SponsorStudentDetailAPIView


app_name = 'sponsorships'

urlpatterns = [
    path('create/', SponsorStudentCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', SponsorStudentDetailAPIView.as_view(), name='detail'),

]
