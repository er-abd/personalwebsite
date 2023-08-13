# Generated by Django 4.1 on 2022-08-26 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_alter_featured_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, default='programmer-icon-defult-min.svg', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='featured_project',
            name='image',
            field=models.ImageField(blank=True, default='project_defult-min.svg', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(blank=True, default='programmer-icon-defult-min.svg', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, default='job-icon-defult.svg', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default='project_defult-min.svg', null=True, upload_to='images'),
        ),
    ]
