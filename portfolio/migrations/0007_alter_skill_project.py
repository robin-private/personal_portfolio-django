# Generated by Django 4.1.7 on 2023-03-13 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_skill_project_alter_project_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_skills', to='portfolio.project'),
        ),
    ]
