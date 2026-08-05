from django.db import models

class Testimony(models.Model):
    author_name = models.CharField(max_length=200)
    author_role = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author_name}"