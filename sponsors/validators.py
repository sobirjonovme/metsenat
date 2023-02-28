from rest_framework.exceptions import ValidationError
from sponsors.models import YURIDIK, JISMONIY


def validate_total_money(value):
    min_money_amount = 1_000_000
    if value < min_money_amount:
        raise ValidationError('Possible minimum money amount is 1,000,000 UZS')


def validate_organization(data):
    if data['type'] == YURIDIK and data.get('organization', '') == '':
        raise ValidationError({
            'organization': "Organization name is required!"
        })
    if data['type'] == JISMONIY and data.get('organization', '') != '':
        raise ValidationError({
            'organization': "Cannot have organization name!"
        })
