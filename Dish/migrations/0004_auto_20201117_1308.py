# Generated by Django 3.1.3 on 2020-11-17 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dish', '0003_auto_20201117_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuisine',
            name='type',
            field=models.CharField(choices=[('Indian', 'Indian'), ('American', 'American'), ('Chinese', 'Chinese'), ('Italian', 'Italian')], default='American', max_length=20),
        ),
    ]
