# Generated by Django 4.2.5 on 2023-09-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudsApp', '0002_profile_is_alive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='def.png', upload_to='prof_pic/'),
        ),
    ]