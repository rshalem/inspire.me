# Generated by Django 3.1 on 2020-08-19 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200818_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
