from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from sponsorships.models import SponsorStudent
from sponsorships.validators import sponsorship_money_validator
from students.models import Student
from sponsors.models import Sponsor
from sponsors.api.serializers import SponsorSerializer


class SponsorStudentSerializer(serializers.ModelSerializer):
    sponsor = SponsorSerializer(read_only=True)
    sponsor_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = SponsorStudent
        fields = ('id', 'sponsor', 'sponsor_id', 'student', 'money_amount')

    def validate_money_amount(self, value):
        if value < 50_000:
            raise ValidationError('Minimum money amount is 50,000 UZS')
        return value

    def create(self, validated_data):
        print(validated_data)
        student = validated_data['student']
        print(123)
        sponsor = get_object_or_404(Sponsor.objects.all(), id=validated_data['sponsor_id'])
        money_amount = validated_data['money_amount']

        # is money amount is valid
        sponsorship_money_validator(sponsor, student, money_amount)

        student.received_money += money_amount
        student.save()

        sponsor.spent_money += money_amount
        sponsor.save()
        
        return super().create(validated_data)

    def update(self, instance, validated_data):
        student = instance.student

        # Check if student is changed or not
        if student != validated_data['student']:
            raise ValidationError({
                'student': 'You cannot change student!'
            })

        old_sponsor = instance.sponsor

        # remove old money amounts from sponsor and user
        old_sponsor.spent_money -= instance.money_amount
        student.received_money -= instance.money_amount

        money_amount = validated_data['money_amount']

        if old_sponsor.id == validated_data['sponsor_id']:
            """ If sponsor is not changed """
            sponsorship_money_validator(old_sponsor, student, money_amount)
            old_sponsor.spent_money += money_amount
        else:
            """ If sponsor is also changed """
            new_sponsor = get_object_or_404(Sponsor.objects.all(), id=validated_data['sponsor_id'])
            sponsorship_money_validator(new_sponsor, student, money_amount)
            new_sponsor.spent_money += money_amount
            new_sponsor.save()

        old_sponsor.save()
        student.received_money += money_amount
        student.save()

        return super().update(instance, validated_data)


# DASHBOARD SERIALIZERS
# Students Statistics
class DashboardStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('full_name', 'created_at')


# Students Statistics
class DashboardSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('full_name', 'created_at')
