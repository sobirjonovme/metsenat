from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from sponsors.models import Sponsor, JISMONIY, YURIDIK


class CreateSponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsor
        fields = ('full_name', 'phone_number', 'total_money', 'type', 'organization')

    def validate_total_money(self, value):
        min_money_amount = 1_000_000
        if value < min_money_amount:
            raise ValidationError('Possible minimum money amount is 1,000,000 UZS')

        return value

    def validate(self, data):

        if data['type'] == YURIDIK and data.get('organization') is None:
            raise ValidationError({
                'organization': "Organization name is required!"
            })
        if data['type'] == JISMONIY and data.get('organization') is not None:
            raise ValidationError({
                'organization': "Cannot have organization name!"
            })

        return data
