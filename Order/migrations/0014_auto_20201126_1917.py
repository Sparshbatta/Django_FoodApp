# Generated by Django 3.1.3 on 2020-11-26 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0013_auto_20201126_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='order',
            name='placed_date',
            field=models.CharField(default='', max_length=60),
        ),
    ]
