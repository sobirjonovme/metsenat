from django.db import models

from students.models import Student
from sponsors.models import Sponsor


# Create your models here.
class SponsorStudent(models.Model):
    sponsor = models.ForeignKey(
        Sponsor,
        on_delete=models.CASCADE,
        related_name='sponsorships'
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='sponsors'
    )
    money_amount = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.money_amount} for {self.student} from {self.sponsor}"
