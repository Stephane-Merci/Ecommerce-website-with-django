# Generated by Django 4.2.6 on 2023-11-27 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_product_life_alter_product_stock_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='long_description',
            field=models.TextField(blank=True, default='This is the long description', null=True),
        ),
    ]
