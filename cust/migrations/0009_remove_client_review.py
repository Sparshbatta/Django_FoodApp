# Generated by Django 3.1.3 on 2020-11-27 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cust', '0008_client_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='review',
        ),
    ]
