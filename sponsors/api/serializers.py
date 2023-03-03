from rest_framework import serializers

from sponsors.models import Sponsor
from sponsors import validators as sp_validators


class RegisterSponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsor
        fields = ('id', 'full_name', 'phone_number', 'total_money', 'type', 'organization')
        extra_kwargs = {
            'total_money': {'validators': [sp_validators.validate_total_money]}
        }

    def validate(self, data):
        sp_validators.validate_organization(data)
        return data


class SponsorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsor
        fields = (
            'id', 'full_name', 'phone_number', 'total_money', 'spent_money', 'payment_type',
            'type', 'status', 'organization', 'created_at',
        )
        read_only_fields = ('spent_money', 'created_at', )
        extra_kwargs = {
            'total_money': {'validators': [sp_validators.validate_total_money]}
        }

    def validate(self, data):
        sp_validators.validate_organization(data)
        return data
