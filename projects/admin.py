from django.contrib import admin
from .models import PersonalInfo, Project, TechStack


admin.site.register(Project)
admin.site.register(PersonalInfo)
admin.site.register(TechStack)
# Register your models here.
