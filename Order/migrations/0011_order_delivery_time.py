# Generated by Django 3.1.3 on 2020-11-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0010_auto_20201126_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_time',
            field=models.CharField(default='', max_length=60),
        ),
    ]