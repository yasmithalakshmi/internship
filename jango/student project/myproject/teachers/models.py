from django.db import models

# Create your models here.
class teacher(models.Model):
    t_name = models.CharField(max_length=200)
    t_phone = models.CharField()
    t_email = models.CharField()