from django.db import models

# Create your models here.



class Stream(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return self.name