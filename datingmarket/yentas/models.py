from django.db import models

# Imports client-to-client comparison algorithms
from clientcomparison import *

class Demography(models.Model):
    country = models.CharField(max_length=200, primary_key=True, default="USA") # Every country in the world belongs to America

    populationM1824 = models.IntegerField(default=0)
    populationM2534 = models.IntegerField(default=0)
    populationM3544 = models.IntegerField(default=0)
    populationM4554 = models.IntegerField(default=0)
    populationM5564 = models.IntegerField(default=0)
    populationM65 = models.IntegerField(default=0)

    populationF1824 = models.IntegerField(default=0)
    populationF2534 = models.IntegerField(default=0)
    populationF3544 = models.IntegerField(default=0)
    populationF4554 = models.IntegerField(default=0)
    populationF5564 = models.IntegerField(default=0)
    populationF65 = models.IntegerField(default=0)

    populationNB1824 = models.IntegerField(default=0)
    populationNB2534 = models.IntegerField(default=0)
    populationNB3544 = models.IntegerField(default=0)
    populationNB4554 = models.IntegerField(default=0)
    populationNB5564 = models.IntegerField(default=0)
    populationNB65 = models.IntegerField(default=0)