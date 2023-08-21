from django.db import models

# Create your models here.

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
    


class Trait(models.Model):
    idNum = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    frequencyM1824 = models.IntegerField(default=0)
    frequencyM2534 = models.IntegerField(default=0)
    frequencyM3544 = models.IntegerField(default=0)
    frequencyM4554 = models.IntegerField(default=0)
    frequencyM5564 = models.IntegerField(default=0)
    frequencyM65 = models.IntegerField(default=0)

    frequencyF1824 = models.IntegerField(default=0)
    frequencyF2534 = models.IntegerField(default=0)
    frequencyF3544 = models.IntegerField(default=0)
    frequencyF4554 = models.IntegerField(default=0)
    frequencyF5564 = models.IntegerField(default=0)
    frequencyF65 = models.IntegerField(default=0)

    frequencyNB1824 = models.IntegerField(default=0)
    frequencyNB2534 = models.IntegerField(default=0)
    frequencyNB3544 = models.IntegerField(default=0)
    frequencyNB4554 = models.IntegerField(default=0)
    frequencyNB5564 = models.IntegerField(default=0)
    frequencyNB65 = models.IntegerField(default=0)

    def __str__(self):
        return self.idNum

class EndUser(models.Model):
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
    maxDistance = models.IntegerField(default=100) # in...kilometers?
    country = models.CharField(max_length=200, primary_key=True, default="USA") # Every country in the world belongs to America

    birthday = models.DateField()
    age = models.IntegerField(default=0)
    maxAge = models.IntegerField(default=20)
    minAge = models.IntegerField(default=20)
    hashedCreditCard = models.CharField(max_length=200)
    dateMeDocs = models.CharField() #the URL where profile/date-me-docs are stored

    def __str__(self):
        return self.idNum

class Matchmaker(models.Model):
    idNum = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=200)
    hashedPassword = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.idNum


# we're just gonna rewrite this one
class Contract(models.Model):
    idNum = models.BigAutoField(primary_key=True)
    isActive = models.BooleanField(default=False)
    endUser = models.OneToOneField(EndUser, on_delete=models.CASCADE)

    totalCost = models.IntegerField(default=0)
    cutToBidder = models.DecimalField(default=0, max_digits = 3, decimal_places = 2)
    cutToInviter = models.DecimalField(default=0, max_digits = 3, decimal_places = 2)
    cutToCompany = models.DecimalField(default=0, max_digits = 3, decimal_places = 2)
    matchmakerCut = 1 - (cutToBidder + cutToInviter + cutToCompany)

    def __str__(self):
        return self.idNum

class totalContractPayout(models.Manager):
    def getPayout(self, aliceContract, bobContract):
        totalPayout = aliceContract.matchmakerCut + bobContract.matchmakerCut

class outstandingBid(models.Manager):
    contractID = models.BigNumberField(primary_key=True) # Should be contract's ID number
    clientID = models.BigNumberField() # Should be client's ID number
    bidderID = models.BigNumberField() # Should be bidder's ID number
    def __str__(self):
        return self.contractID

class Match(models.Manager):

    @classmethod
    def create(self, Alice, Bob): # also compatibility score


        self.create(matchPayout = totalContractPayout.getPayout(Alice.activeContract, Bob.activeContract))