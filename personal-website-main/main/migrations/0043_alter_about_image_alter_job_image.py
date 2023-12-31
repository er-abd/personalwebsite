# Generated by Django 4.1 on 2022-08-27 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_alter_about_image_alter_featured_project_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.URLField(blank=True, default='https://i.imgur.com/LWbrALG.jpg', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.URLField(blank=True, default='https://cdn.iconfinder.com/icons/5094713/5568693/512/raster.png?token=1661631238-WeLYOs4bm1fv07Kk%2Fc%2FUWLI4112vEkh5lkVKQUGAEs0%3D', max_length=400, null=True),
        ),
    ]
