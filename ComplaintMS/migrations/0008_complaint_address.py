# Generated by Django 3.2.2 on 2024-07-07 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComplaintMS', '0007_alter_complaint_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
