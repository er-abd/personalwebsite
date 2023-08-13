# Generated by Django 4.1 on 2022-08-27 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.URLField(blank=True, default='https://cdn.iconfinder.com/icons/396751/798258/512/raster.png?token=1661628488-O24rBHLTnp1Pptw5VSZqWQAxGf62Giu3afUw8ZVnrzM%3D', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='featured_project',
            name='image',
            field=models.URLField(blank=True, default='https://cdn.iconfinder.com/icons/396751/798258/512/raster.png?token=1661628488-O24rBHLTnp1Pptw5VSZqWQAxGf62Giu3afUw8ZVnrzM%3D', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.URLField(blank=True, default='https://cdn.iconfinder.com/icons/396751/798258/512/raster.png?token=1661628488-O24rBHLTnp1Pptw5VSZqWQAxGf62Giu3afUw8ZVnrzM%3D', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.URLField(blank=True, default='https://cdn.iconfinder.com/icons/396751/798258/512/raster.png?token=1661628488-O24rBHLTnp1Pptw5VSZqWQAxGf62Giu3afUw8ZVnrzM%3D', max_length=400, null=True),
        ),
    ]