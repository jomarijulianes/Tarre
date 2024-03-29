# Generated by Django 4.2.6 on 2023-12-02 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_framework_frontend_framework_delete_programming'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frontend_Stack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(blank=True)),
                ('version', models.TextField(blank=True)),
                ('release_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
