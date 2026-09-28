from django.db import models

# Create your models here.
from django.db import models

from django.db import models

class emp(models.Model):
    e_name = models.CharField(max_length=100)
    e_phone = models.CharField()
    e_id = models.IntegerField()