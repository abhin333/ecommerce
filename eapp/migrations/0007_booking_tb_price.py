# Generated by Django 4.0.1 on 2022-02-15 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0006_alter_seller_tb_authn'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_tb',
            name='price',
            field=models.CharField(default='', max_length=100),
        ),
    ]
