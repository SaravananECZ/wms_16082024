# Generated by Django 5.0.6 on 2024-07-30 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]