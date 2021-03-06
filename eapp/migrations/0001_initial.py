# Generated by Django 4.0.1 on 2022-01-31 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='seller_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(default='', max_length=10)),
                ('uname', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='user_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10)),
                ('username', models.CharField(default='', max_length=10)),
                ('email', models.CharField(default='', max_length=10)),
                ('password', models.CharField(default='', max_length=10)),
                ('phone_no', models.CharField(default='', max_length=10)),
                ('booking_id', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
