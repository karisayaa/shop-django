# Generated by Django 2.1.7 on 2020-07-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.CharField(max_length=2000),
        ),
    ]
