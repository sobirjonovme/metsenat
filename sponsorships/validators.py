from rest_framework.exceptions import ValidationError


def sponsorship_money_validator(sponsor, student, money_amount):
    if student.received_money + money_amount > student.tuition_fee:
        raise ValidationError({
            'money_amount': "Given money is more than the student need!"
        })
    if sponsor.spent_money + money_amount > sponsor.total_money:
        raise ValidationError({
            'money_amount': "Given money is more than sponsor balance!"
        })
