from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from students.models import University, Student


class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = ('id', 'name')


class StudentSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)

    university_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ('received_money', 'created_at')

    def validate_tuition_fee(self, value):
        if value < 500_000:
            raise ValidationError('Tuition fee cannot be less than 500,000 UZS')
        return value
