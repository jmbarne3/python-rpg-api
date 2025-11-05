from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    desc = models.CharField(max_length=255, blank=True, null=True)
