from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from sponsors.models import Sponsor
from sponsors import validators as sp_validators


class RegisterSponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsor
        fields = ('full_name', 'phone_number', 'total_money', 'type', 'organization')
        extra_kwargs = {
            'total_money': {'validators': [sp_validators.validate_total_money]}
        }

    # def validate_total_money(self, value):
    #     min_money_amount = 1_000_000
    #     if value < min_money_amount:
    #         raise ValidationError('Possible minimum money amount is 1,000,000 UZS')
    #
    #     return value

    def validate(self, data):
        sp_validators.validate_organization(data)
        return data


class SponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsor
        fields = '__all__'
        read_only_fields = ('spent_money', 'created_at', )
        extra_kwargs = {
            'total_money': {'validators': [sp_validators.validate_total_money]}
        }

    def validate(self, data):
        sp_validators.validate_organization(data)
        return data
