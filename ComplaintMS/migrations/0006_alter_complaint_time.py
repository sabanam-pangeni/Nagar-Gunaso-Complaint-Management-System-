# Generated by Django 3.2.2 on 2024-07-02 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComplaintMS', '0005_auto_20240621_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='Time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]