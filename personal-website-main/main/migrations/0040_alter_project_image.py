# Generated by Django 4.1 on 2022-08-27 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.URLField(blank=True, default='https://drive.google.com/file/d/1MMMIzqAfSptZNvI3T1gNh12w1qcx45zZ/view?usp=sharing', max_length=400, null=True),
        ),
    ]
