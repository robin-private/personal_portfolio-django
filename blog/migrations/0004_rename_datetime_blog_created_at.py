# Generated by Django 4.1.7 on 2023-03-07 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_datetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='datetime',
            new_name='created_at',
        ),
    ]
