# Generated by Django 4.1 on 2022-08-25 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_technical_skills_technical_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professional_Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
