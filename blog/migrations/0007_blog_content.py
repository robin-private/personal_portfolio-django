# Generated by Django 4.1.7 on 2023-03-07 10:38

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.CharField(default=builtins.print, max_length=2500),
            preserve_default=False,
        ),
    ]