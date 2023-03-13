# Generated by Django 4.1.7 on 2023-03-07 10:11

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.CharField(default=blog.models.get_default_created_at, max_length=50),
        ),
    ]
