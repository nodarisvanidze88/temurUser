# Generated by Django 5.0.6 on 2024-06-06 23:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_temurusers_email_alter_temurusers_tel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='temurusers',
            name='registration',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]