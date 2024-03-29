# Generated by Django 4.2.6 on 2024-02-02 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0021_remove_classification_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classification',
            name='price_range',
        ),
        migrations.AddField(
            model_name='laptop',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='classification',
            name='laptop',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webapp.laptop', to_field='price'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='price',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]
