# Generated by Django 4.2.6 on 2023-12-09 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_ide'),
    ]

    operations = [
        migrations.AddField(
            model_name='ide',
            name='Description',
            field=models.TextField(blank=True),
        ),
    ]