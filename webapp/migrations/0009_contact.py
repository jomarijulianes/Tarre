# Generated by Django 4.2.6 on 2023-12-08 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_frontend_stack'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('mobile', models.IntegerField(blank=True)),
                ('message', models.TextField(blank=True)),
                ('release_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
