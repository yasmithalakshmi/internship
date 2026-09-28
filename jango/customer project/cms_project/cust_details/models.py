from django.db import models

# Create your models here.
class cust_detail(models.Model):
    c_name = models.CharField(max_length=200)
    c_phone = models.CharField()
    c_email = models.CharField()

