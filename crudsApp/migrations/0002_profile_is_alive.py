# Generated by Django 4.2.5 on 2023-09-24 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_alive',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
