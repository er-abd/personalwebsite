# Generated by Django 4.1 on 2022-08-27 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_alter_about_image_alter_featured_project_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, default='job-icon-defult-min.svg', null=True, upload_to='images'),
        ),
    ]