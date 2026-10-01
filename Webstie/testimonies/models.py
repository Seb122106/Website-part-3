from django.db import models


class Testimony(models.Model):
    full_name = models.CharField(max_length=100, default = "Anonymous")
    content = models.TextField()

    def __str__(self):
        return self.full_name