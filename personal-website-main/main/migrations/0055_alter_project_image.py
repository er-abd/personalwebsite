# Generated by Django 4.1 on 2022-08-27 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0054_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.URLField(blank=True, default='https://cdn4.iconfinder.com/data/icons/thin-line-icons-for-seo-and-development-1/64/seo_programming-512.png', max_length=400, null=True),
        ),
    ]
