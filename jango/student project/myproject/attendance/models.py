from django.db import models

# Create your models here.
class attend(models.Model):
    s_name = models.CharField(max_length=200)
    s_attend_percentage = models.CharField()