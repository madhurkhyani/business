# Generated by Django 5.1 on 2025-01-01 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('home', '0005_alter_cash_in_options_alter_cash_out_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cash_in',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.clientdata'),
        ),
        migrations.AddField(
            model_name='cash_out',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.clientdata'),
        ),
    ]
