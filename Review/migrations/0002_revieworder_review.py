# Generated by Django 3.1.3 on 2020-11-27 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='revieworder',
            name='review',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
    ]
