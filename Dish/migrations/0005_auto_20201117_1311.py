# Generated by Django 3.1.3 on 2020-11-17 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dish', '0004_auto_20201117_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuisine',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]