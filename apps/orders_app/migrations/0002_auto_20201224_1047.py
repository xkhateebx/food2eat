# Generated by Django 2.2.4 on 2020-12-24 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='order',
            name='checked_out',
            field=models.BooleanField(default=False),
        ),
    ]