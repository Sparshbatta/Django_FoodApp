# Generated by Django 3.1.3 on 2020-11-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0009_auto_20201126_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='placed_time',
            field=models.CharField(default='', max_length=60),
        ),
    ]
