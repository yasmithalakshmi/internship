from django.db import models

# Create your models here.
class student(models.Models):
    s_name = models.charFeild(max_length=200)
    s_phone = models.charField()
    s_email = models.charField()
    s_marks= models.integerField()
    