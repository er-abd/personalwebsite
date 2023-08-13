import re
from .models import About, Education, Featured_Project, Job, Home, Professional_Skill, Tag, Technical_Skill, Work_Experience, Project, Categorie
import email
from email import message
from django.contrib import messages
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


# Create your views here.


def home(request):
    things_i_do = Job.objects.all()
    home_details = Home.objects.all()
    about_details = About.objects.all()
    tags = About.objects.all()
    f_projects = Featured_Project.objects.all()
    t_skills = Technical_Skill.objects.all()
    p_skills = Professional_Skill.objects.all()
    education = Education.objects.all()
    works = Work_Experience.objects.all()
    projects = Project.objects.all()
    categories = Categorie.objects.all()

    context = {'things_i_do': things_i_do,
               'home_details': home_details, 'about_details': about_details, 'tags': tags, 'f_projects': f_projects,
               't_skills': t_skills, 'p_skills': p_skills, 'education': education, 'works': works, 'projects': projects,
               'categories': categories
               }

    return render(request, 'main/index.html', context)


def sendEmail(request):

    if request.method == 'POST':
        template = render_to_string('main/email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['django.test.website@outlook.com']

        )
        email.fail_silently = False
        email.send()

    return render(request, 'main/email_sent.html')
