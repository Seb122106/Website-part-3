from django.db import models
from django.db.models.functions import Lower

class TechStack (models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(
                Lower('name'),
                name = 'unique_techstack_name_ci',
                violation_error_message = 'This TeckStack already exists.',
            ),
        ]
    def __str__ (self):
        return self.name
class Project(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tech_stacks = models.ManyToManyField(TechStack, related_name='projects')

    class Meta:
        ordering = ['-created_at', '-id']

    def __str__(self):
        return self.project_name

    @property
    def tech_stack_names(self):
        return ', '.join(stack.name for stack in self .tech_stacks.all())
    
class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    summary = models.TextField()
    contact_number = models.CharField(max_length=20)
    contact_email = models.EmailField(max_length=200)
    address = models.TextField()

    class Meta:
        verbose_name_plural = 'PersonalInfo'

    @property
    def full_name(self):
        return f'{self.first_name, self.last_name}'


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
