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

    def __str__(self):
        return self.country

class Client(models.Model):
    idNum = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=200)
    hashedPassword = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    class Gender(models.IntegerChoices):
        MALE = 2
        FEMALE = 3
        NONBINARY = 5
    class InterestedIn(models.IntegerChoices):
        M = 2
        F = 3
        NB = 5
        MF = 6
        MNB = 10
        FNB = 15
        MFNB = 30
    gender = models.integerField(choices=Gender.choices)
    orientation = models.integerField(choices=InterestedIn.choices)

    homeLatitude = models.DecimalField(max_digits = 9, decimal_places = 3)
    homeLongitude = models.DecimalField(max_digits = 9, decimal_places = 3)
    maxDistance = models.IntegerField(default=100) # Input can be in miles but we will change to kilometers for production code
    country = models.CharField(max_length=200, primary_key=True, default="USA") # Every country in the world belongs to America

    birthday = models.DateField()
    age = models.IntegerField(default=0)
    minAge = models.IntegerField(default=(self.age / 2) + 7)
    maxAge = models.IntegerField(default=(self.age - 7) * 2)

    hashedCreditCard = models.CharField(max_length=200)
    dateMeDocs = models.CharField() #the URL where the date-me-docs are stored
    # 'where the date-me-docs are stored' demands a BHotR pun in production code

    def __str__(self):
        return self.username

# Bounty and Contract get split

class Bounty(models.Model):
    idNum = models.BigAutoField(primary_key=True)
    isActive = models.BooleanField(default=True)

    # Presumably the history of all bounties will be stored, so a client can have multiple associated bounties, but any bounty can have only one associated client
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    # Validators may not work here but we'll see
    bountyCost = models.decimalField(max_digits = 5, decimal_places = 2, default = 2.50, validators=[
            MaxValueValidator(999.99),
            MinValueValidator(2.50) 
        ])
    
    #make sure this is UTC/absolute time
    #Expiration date rather than 'X a week' because people can (maybe?) only ever have one active bounty out.
    # or rather, maybe they don't. obviously bounties need an expiration date whether those are user-chosen or by fiat
    bountyPostDate = models.DateTimeField()
    bountyExpirationDate = models.DateTimeField()

    initialBidderCut = models.decimalField(max_digits = 3, decimal_places = 2, default = 0.10, validators=[
        MaxValueValidator(0.99),
        MinValueValidator(0.01)
        ]) # Default should be low, 5-10%, and not messed with unless there is good reason to, the value validators are just for sanity checking


    






