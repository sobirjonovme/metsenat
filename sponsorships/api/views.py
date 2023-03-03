from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import models

from students.models import Student
from sponsors.models import Sponsor
from sponsorships.models import SponsorStudent
from sponsorships.api.serializers import SponsorStudentSerializer, DashboardSponsorSerializer, DashboardStudentSerializer


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


# DASHBOARD VIEWS
# Overall Sponsorship Statistics
class OverallStatistics(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        sponsorship_money = Sponsor.objects.aggregate(total_sponsorship_money=models.Sum('spent_money'))
        required_money = Student.objects.aggregate(total_required_money=models.Sum('tuition_fee'))

        total_sponsorship_money = sponsorship_money['total_sponsorship_money']
        total_required_money = required_money['total_required_money']

        rest_required_money = total_required_money - total_sponsorship_money

        return Response({'total_sponsorship_money': total_sponsorship_money,
                         'total_required_money': total_required_money,
                         'rest_required_amount': rest_required_money})


# Dashboard Student Statistics
class SponsorStatistics(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = DashboardSponsorSerializer

    permission_classes = [IsAuthenticated]


# Dashboard Student Statistics
class StudentStatistics(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = DashboardStudentSerializer

    permission_classes = [IsAuthenticated]
