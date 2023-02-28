from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView

from sponsors.models import Sponsor
from sponsors.api.serializers import RegisterSponsorSerializer, SponsorSerializer


class RegisterSponsorAPIView(CreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = RegisterSponsorSerializer


class SponsorListAPIView(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsorDetailAPIView(RetrieveUpdateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
