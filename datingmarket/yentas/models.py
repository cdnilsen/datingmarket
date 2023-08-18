from django.db import models

# Create your models here.

def compareOrienders(alice, bob):
    return (((bob.orientation % alice.gender) == 0) and ((alice.orientation % bob.gender) == 0))

def compareAges(alice, bob): # 8)
    return ((alice.age >= bob.minAge) and (alice.age <= bob.maxAge) and (bob.age >= alice.minAge) and (bob.age <= alice.maxAge))

class Trait(models.Model):
    idNum = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.idNum

class EndUser(models.Model):
    idNum = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=200)
    hashedPassword = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    class Gender(models.IntergerChoices):
        MALE = 2
        FEMALE = 3
        NONBINARY = 5
    class InterestedIn(models.IntergerChoices):
        M = 2
        F = 3
        NB = 5
        MF = 6
        MNB = 10
        FNB = 15
        MFNB = 30
    gender = models.integerField(choices=Gender.choices)
    orientation = models.integerField(choices=InterestedIn.choices)

    maxAge = models.IntegerField(default=20)
    minAge = models.IntegerField(default=20)
    hashedCreditCard = models.CharField(max_length=200)
    dateMeDocs = models.string #the URL, presumably

    originalMatchmaker = models.ForeignKey(Matchmaker, on_delete=models.CASCADE)

    activeContract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    def __str__(self):
        return self.idNum







class Matchmaker(models.Model):
    idNum = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=200)
    hashedPassword = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.idNum

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


class Match(models.Manager):

    @classmethod
    def create(self, Alice, Bob): # also compatibility score


        self.create(matchPayout = totalContractPayout.getPayout(Alice.activeContract, Bob.activeContract))