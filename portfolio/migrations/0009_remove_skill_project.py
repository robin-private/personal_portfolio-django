# Generated by Django 4.1.7 on 2023-03-13 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_alter_project_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='project',
        ),
    ]
