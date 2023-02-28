from rest_framework.generics import CreateAPIView

from sponsors.models import Sponsor
from sponsors.api.serializers import RegisterSponsorSerializer


class RegisterSponsorAPIView(CreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = RegisterSponsorSerializer
