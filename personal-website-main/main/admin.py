from django.contrib import admin

# Register your models here.

from .models import Home, Job, About, Tag, Featured_Project, Technical_Skill, Professional_Skill, Education, Work_Experience, Project, Categorie


admin.site.register(Job)
admin.site.register(Home)
admin.site.register(About)
admin.site.register(Tag)
admin.site.register(Featured_Project)
admin.site.register(Technical_Skill)
admin.site.register(Professional_Skill)
admin.site.register(Education)
admin.site.register(Work_Experience)
admin.site.register(Project)
admin.site.register(Categorie)
