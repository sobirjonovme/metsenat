from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from users.api.serializers import RegistrationSerializer
from users.models import CustomUser


class RegistrationAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer


class LogOutAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        request.user.auth_token.delete()

        return Response(
            data={'message': 'You logged out successfully!'},
            status=status.HTTP_200_OK
        )
