# Generated by Django 4.1 on 2022-08-27 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_alter_about_image_alter_home_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.URLField(blank=True, default='https://cdn.iconfinder.com/icons/756827/1180797/512/raster.png?token=1661629654-YZr0kqRHoyy6YvT5t2CJP5OxXcbb5ks3LMhseeny2Wk%3D', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.URLField(blank=True, default='https://cdn.iconfinder.com/icons/756827/1180797/512/raster.png?token=1661629654-YZr0kqRHoyy6YvT5t2CJP5OxXcbb5ks3LMhseeny2Wk%3D', max_length=400, null=True),
        ),
    ]
