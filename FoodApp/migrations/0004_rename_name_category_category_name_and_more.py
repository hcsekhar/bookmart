# Generated by Django 4.1 on 2024-10-07 06:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0003_category_alter_food_created_at_food_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category_name',
        ),
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='food',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 7, 11, 35, 2, 785459)),
        ),
        migrations.CreateModel(
            name='sub_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_image', models.ImageField(upload_to='')),
                ('sub_category_name', models.CharField(max_length=100)),
                ('main_category', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='FoodApp.category')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='sub_categories',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='FoodApp.sub_category'),
        ),
    ]
