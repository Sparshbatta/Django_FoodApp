# Generated by Django 3.1.3 on 2020-11-17 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dish', '0006_auto_20201117_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainDish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('type', models.CharField(choices=[('Indian', 'Indian'), ('American', 'American'), ('Chinese', 'Chinese'), ('Italian', 'Italian')], default='American', max_length=20)),
                ('desc', models.TextField(max_length=200)),
                ('image', models.FileField(upload_to='dishes/images/')),
                ('price', models.FloatField(default=0.0)),
            ],
        ),
        migrations.DeleteModel(
            name='Cuisine',
        ),
    ]
