from django.db import models

# Create your models here.
class Characters(models.Model):
    c_name = models.CharField(max_length=50)
    #c_image= models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.c_name