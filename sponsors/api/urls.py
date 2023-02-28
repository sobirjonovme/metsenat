from django.urls import path

from sponsors.api.views import RegisterSponsorAPIView


app_name = 'sponsors'

urlpatterns = [
    path('register/', RegisterSponsorAPIView.as_view(), name='register'),

]
