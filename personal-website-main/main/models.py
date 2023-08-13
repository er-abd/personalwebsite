from ctypes import addressof
from distutils.command.upload import upload
import email
from email.policy import default
from modulefinder import Module
from re import T
from statistics import mode
from tokenize import blank_re
from django.db import models

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(max_length=400, null=True, blank=True,
                            default="https://cdn2.iconfinder.com/data/icons/picol-vector/32/source_code-256.png")
    description = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Home(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=1000)
    email = models.EmailField(max_length=500)
    telephone = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    social_facebook = models.CharField(max_length=400, null=True, blank=True)
    social_twitter = models.CharField(max_length=400, null=True, blank=True)
    social_githup = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.name


class About(models.Model):
    description = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True)
    cv_link = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.description


class Featured_Project(models.Model):
    type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=3000, null=True, blank=True)
    project_githup = models.CharField(max_length=400, null=True, blank=True)
    project_live = models.CharField(max_length=400, null=True, blank=True)
    image = models.URLField(max_length=400, null=True, blank=True,
                            default="https://cdn4.iconfinder.com/data/icons/thin-line-icons-for-seo-and-development-1/64/seo_programming-512.png")

    def __str__(self):
        return self.description


class Technical_Skill(models.Model):
    name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Professional_Skill(models.Model):
    name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Education(models.Model):
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    date = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.title


class Work_Experience(models.Model):
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    date = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.title


class Categorie(models.Model):
    type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.type)


class Project(models.Model):
    type = models.ForeignKey(
        Categorie, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=10000, null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True)
    project_githup = models.CharField(max_length=400, null=True, blank=True)
    project_live = models.CharField(max_length=400, null=True, blank=True)
    image = models.URLField(max_length=400, null=True, blank=True,
                            default="https://cdn4.iconfinder.com/data/icons/thin-line-icons-for-seo-and-development-1/64/seo_programming-512.png")
    screenshot_1 = models.URLField(max_length=400, null=True, blank=True)
    screenshot_1_description = models.CharField(
        max_length=2000, null=True, blank=True)
    screenshot_2 = models.URLField(max_length=400, null=True, blank=True)
    screenshot_2_description = models.CharField(
        max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name
