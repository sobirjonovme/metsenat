from django.urls import path

from sponsors.api.views import RegisterSponsorAPIView, SponsorDetailAPIView, SponsorListAPIView


app_name = 'sponsors'

urlpatterns = [
    path('', SponsorListAPIView.as_view(), name='list'),
    path('<int:pk>/', SponsorDetailAPIView.as_view(), name='detail'),
    path('register/', RegisterSponsorAPIView.as_view(), name='register'),

]
