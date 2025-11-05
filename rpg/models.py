from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    desc = models.CharField(max_length=255, blank=True, null=True)
    exp = models.IntegerField(null=False, blank=False, default=1)

    def __str__(self):
        """
        Override the string function for the admin
        """
        return self.name
