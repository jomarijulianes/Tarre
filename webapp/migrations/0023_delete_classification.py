# Generated by Django 4.2.6 on 2024-02-02 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0022_remove_classification_price_range_laptop_description_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Classification',
        ),
    ]
