from django.utils import timezone
from django.db import models


# Create your models here.
BACHELOR, MASTER = ('BS', 'MS')

STUDENT_TYPES = (
    (BACHELOR, 'Bakalavr'),
    (MASTER, 'Magistr')
)


class University(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=13)
    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        related_name='students'
    )
    type = models.CharField(max_length=2, choices=STUDENT_TYPES, default=BACHELOR)
    tuition_fee = models.DecimalField(max_digits=12, decimal_places=2)
    received_money = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.full_name
