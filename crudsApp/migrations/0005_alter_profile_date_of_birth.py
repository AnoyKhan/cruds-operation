# Generated by Django 4.2.5 on 2023-09-26 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudsApp', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.CharField(max_length=10),
        ),
    ]
