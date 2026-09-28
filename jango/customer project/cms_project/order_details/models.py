from django.db import models

# Create your models here.
class order(models.Model):
    o_name = models.CharField(max_length=200)
    o_id = models.CharField()

