# Generated by Django 4.1 on 2024-10-09 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0009_alter_food_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 9, 13, 9, 37, 617288)),
        ),
    ]
