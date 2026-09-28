from django.db import models

# Create your models here.
class student(models.Model):
    s_name = models.CharField(max_length=200)
    s_phone = models.CharField()
    s_email = models.CharField()
    s_marks = models.IntegerField()