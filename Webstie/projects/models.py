from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=250)
    link = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.project_name
    
class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    summary = models.TextField()
    contact_number = models.CharField(max_length=20)
    contact_email = models.EmailField(max_length=200)
    address = models.TextField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
