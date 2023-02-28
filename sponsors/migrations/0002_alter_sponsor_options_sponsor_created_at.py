# Generated by Django 4.1.7 on 2023-02-28 11:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sponsor',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='sponsor',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]