# Generated by Django 3.1 on 2020-08-20 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_card_date_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='date_published',
        ),
    ]
