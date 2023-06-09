# Generated by Django 4.1.7 on 2023-03-08 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='user/files/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='resume',
            field=models.FileField(blank=True, upload_to='user/files/'),
        ),
    ]
