# Generated by Django 5.1.1 on 2024-12-27 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_data_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_data',
            name='note',
            field=models.CharField(default='', max_length=250),
        ),
    ]