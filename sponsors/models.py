from django.utils import timezone
from django.db import models


JISMONIY, YURIDIK = ('JIS', 'YUR')
NEW, MODERATION, CONFIRMED, CANCELLED = (
    'NEW', 'MOD', 'CNF', 'CNC'
)
CASH, MONEY_TRANSFER = ('CASH', "TRANS")


SPONSOR_TYPES = (
    (JISMONIY, 'Jismoniy shaxs'),
    (YURIDIK, 'Yuridik shaxs')
)
SPONSOR_STATUS = (
    (NEW, 'Yangi'),
    (MODERATION, 'Moderatsiyada'),
    (CONFIRMED, 'Tasdiqlangan'),
    (CANCELLED, 'Bekor qilingan'),
)
PAYMENT_TYPES = (
    (CASH, 'Naqd pul'),
    (MONEY_TRANSFER, "Pul o'tkazmalari")
)


# Create your models here.
class Sponsor(models.Model):
    full_name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=13)
    total_money = models.DecimalField(max_digits=12, decimal_places=2)
    spent_money = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    payment_type = models.CharField(max_length=8, choices=PAYMENT_TYPES, default=MONEY_TRANSFER)
    type = models.CharField(max_length=8, choices=SPONSOR_TYPES, default=JISMONIY)
    status = models.CharField(max_length=8, choices=SPONSOR_STATUS, default=NEW)
    organization = models.CharField(max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.full_name
