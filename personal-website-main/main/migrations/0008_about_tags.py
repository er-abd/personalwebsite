# Generated by Django 4.1 on 2022-08-24 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_about_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='tags',
            field=models.ManyToManyField(null=True, to='main.tag'),
        ),
    ]
