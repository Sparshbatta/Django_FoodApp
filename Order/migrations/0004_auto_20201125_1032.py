# Generated by Django 3.1.3 on 2020-11-25 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0003_auto_20201125_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]