# Generated by Django 2.2.4 on 2020-12-24 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='iconLink',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='meal',
            name='imgLink',
            field=models.TextField(),
        ),
    ]
