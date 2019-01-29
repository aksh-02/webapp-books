# Generated by Django 2.1.4 on 2019-01-19 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='sub_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]
