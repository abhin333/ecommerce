# Generated by Django 4.0.1 on 2022-02-03 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0012_rename_discreption_product_tb_dis'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_tb',
            name='sid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='eapp.seller_tb'),
            preserve_default=False,
        ),
    ]
