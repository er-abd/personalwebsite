# Generated by Django 4.1 on 2022-08-26 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_alter_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default='project_defult.svg', null=True, upload_to='images'),
        ),
    ]
