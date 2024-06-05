# Generated by Django 3.2.2 on 2024-05-23 15:19

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ComplaintMS', '0003_auto_20240520_0708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Branch',
        ),
        migrations.AlterField(
            model_name='complaint',
            name='Type_of_complaint',
            field=models.CharField(choices=[('Fire', 'Fire'), ('Road', 'Road'), ('Garbage', 'Garbage'), ('Transportation', 'Transportation'), ('Other', 'Other')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='grievance',
            name='guser',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='grievance', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='collegename',
            field=models.CharField(default='Default College Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contactnumber',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: Up to 10 digits allowed.', regex='^\\d{10,10}$')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='type_user',
            field=models.CharField(choices=[('resident', 'Resident'), ('admin', 'Admin')], default='resident', max_length=20),
        ),
    ]