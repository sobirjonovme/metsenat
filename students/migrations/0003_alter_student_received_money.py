# Generated by Django 4.1.7 on 2023-03-01 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_university_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='received_money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
