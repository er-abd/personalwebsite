# Generated by Django 4.1 on 2022-08-24 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_job_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=500)),
                ('telephone', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('social_facebook', models.CharField(max_length=400)),
                ('social_twitter', models.CharField(max_length=400)),
                ('social_githup', models.CharField(max_length=400)),
                ('image', models.ImageField(blank=True, default='code-solid.svg', null=True, upload_to='images')),
            ],
        ),
    ]
