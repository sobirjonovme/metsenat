from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from sponsorships.models import SponsorStudent
from sponsorships.api.serializers import SponsorStudentSerializer


class SponsorStudentCreateAPIView(CreateAPIView):
    queryset = SponsorStudent.objects.all()
    serializer_class = SponsorStudentSerializer

    permission_classes = [IsAuthenticated]


class SponsorStudentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SponsorStudent.objects.all()
    serializer_class = SponsorStudentSerializer

    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        # Remove money amounts from student and sponsor
        instance.sponsor.spent_money -= instance.money_amount
        instance.student.received_money -= instance.money_amount
        instance.sponsor.save()
        instance.student.save()

        instance.delete()
