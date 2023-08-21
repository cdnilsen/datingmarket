from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

import datetime
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from birthday import BirthdayField, BirthdayManager

# from dateutil.relativedelta import relativedelta

# Imports client-to-client comparison algorithms
# from .clientcomparison import *

# Built-in User model already has a username, PW, email, first name, last name, date joined, last login, is_superuser, is_active, is_staff, groups (many-to-many), user_permissions (many-to-many)



class Client(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key=True)
    GENDER = [
        (2, "MALE"),
        (3, "FEMALE"),
        (5, "NONBINARY"),
    ]
    INTERESTED_IN = [
        (2, "M"),
        (3, "F"),
        (5, "NB"),
        (6, "MF"),
        (10, "MNB"),
        (15, "FNB"),
        (30, "MFNB"),
    ]

    # When creating Clients in shell, it is possible to give them a gender outside the choices, e.g. 7. Deal with this later
    gender = models.IntegerField(choices=GENDER)
    orientation = models.IntegerField(choices= INTERESTED_IN)

    country = models.CharField(max_length=200, default="USA")


'''
class Matchmaker(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
'''

'''
class SiteUser(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    
    hashedCreditCard = models.CharField(max_length=200)
    birthday = BirthdayField()

    @property 
    def age(self):
        return datetime.(datetime.date.today() - self.birthday).years

    # Every country in the world belongs to America
    # Necessary for matchmakers as well due to finance regs
    country = models.CharField(max_length=200, primary_key=True, default="USA") 
    
    class Meta:
        abstract = True    


# Stores how many users in each gender/age demographic we have in each country
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

class Client(SiteUser):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    age = models.IntegerField(default = 18)
    # DO NOT MESS with the numbers are here. Server uses prime factorization to determine oriender compatibility
    GENDER = [
        (2, "MALE"),
        (3, "FEMALE"),
        (5, "NONBINARY"),
    ]
    INTERESTED_IN = [
        (2, "M"),
        (3, "F"),
        (5, "NB"),
        (6, "MF"),
        (10, "MNB"),
        (15, "FNB"),
        (30, "MFNB"),
    ]
    # These gonna need defaults?
    gender = models.IntegerField(choices=GENDER)
    orientation = models.IntegerField(choices=INTERESTED_IN)

    homeLatitude = models.DecimalField(max_digits = 9, decimal_places = 3)
    homeLongitude = models.DecimalField(max_digits = 9, decimal_places = 3)
    maxDistance = models.IntegerField(default = 100) # Input can be in miles but we will change to kilometers for production code

    minAge = models.IntegerField(default = round((age / 2) + 7))
    maxAge = models.IntegerField(default = (age - 7) * 2)

    dateMeDocs = models.CharField() #the URL where the date-me-docs are stored
    # 'where the date-me-docs are stored' demands a BHotR pun in production code

    def __str__(self):
        return self.idNum

class Matchmaker(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    def __str__(self):
        return self.idNum

class Bounty(models.Model):
    idNum = models.BigAutoField(primary_key=True)
    isActive = models.BooleanField(default=True)

    # Presumably the history of all bounties will be stored, so a client can have multiple associated bounties, but any bounty can have only one associated client
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    originalBidder = models.ForeignKey(Matchmaker, on_delete=models.CASCADE)

    # Validators may not work here but we'll see
    bountyCost = models.DecimalField(max_digits = 5, decimal_places = 2, default = 2.50, validators=[
            MaxValueValidator(999.99),
            MinValueValidator(2.50) 
        ])
    
    #make sure these are UTC/absolute time

    #Expiration date is still probably at the same time every week because the back-market needs to close at the same time on all possible matches. Not sure what we do for multiple time zones: perhaps 1 AM Pacific/4 AM Eastern on (Sunday? Monday? morning)

    bountyPostDate = models.DateTimeField()
    bountyExpirationDate = models.DateTimeField()

    initialBidderCut = models.DecimalField(max_digits = 3, decimal_places = 2, default = 0.10, validators=[
        MaxValueValidator(0.99),
        MinValueValidator(0.01)
        ]) # Default should be low, 5-10%, and not messed with unless there is good reason to, the value validators are just for sanity checking

    successfulMMCut = models.DecimalField(max_digits = 3, decimal_places = 2, default = 0.80, validators=[
        MaxValueValidator(0.99),
        MinValueValidator(0.01)
        ])

    # Cuts to inviters and cuts to the site from the bounties themselves (rather than back-market bids) are not yet final but they're placed here for now
    # If we get rid of these 'em, the remaining defaults all have to add up to 1.00

    # There is surely some way to validate things so that all the cuts add up to 1.00, figure out how to do that later

    inviterCut = models.DecimalField(max_digits = 3, decimal_places = 2, default = 0.05, validators=[
        MaxValueValidator(0.99),
        MinValueValidator(0.01)
        ])

    siteCut = models.DecimalField(max_digits = 3, decimal_places = 2, default = 0.05, validators=[
        MaxValueValidator(0.99),
        MinValueValidator(0.01)
        ])

    def __str__(self):
        return self.idNum

class Match(models.Model):
    idNum = models.BigAutoField(primary_key=True)
    alice = models.ForeignKey(Client, on_delete=models.CASCADE)
    bob = models.ForeignKey(Client, on_delete=models.CASCADE)

    # This is a one-to-many relationship: there may be multiple bids out for (Alice, Bob), (Alice, Charlie), (Alice, Dave), but Alice's bounty is the same for all of those
    aliceBounty = models.ForeignKey(Bounty, on_delete=models.CASCADE)
    bobBounty = models.ForeignKey(Bounty, on_delete=models.CASCADE)

    # Auctions should be normal English (i.e. open bid, highest bid wins) as that's apparently equivalent to a sealed Vickrey, wrt the expected revenue to the auctioneer and the amount paid by the bidder.

    # Default is 0, but placing a bid needs to have a minimum of a penny
    currentTopBid = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0.00, validators = [
        MinValueValidator(0.01)
    ])

    # Bids should be public. Bidders should be hidden to other bidders, however, because otherwise the value in a good matchmaking model is lost (bad MMs will just see that a top-5 MM bid $5 and will then bid $5.01).
    currentTopBidder = models.ForeignKey(Matchmaker, on_delete=models.CASCADE)

    # Final payout is (aliceBounty.successfulMMCut + bobBounty.successfulMMCut) - currentTopBid. This should be shown to the bidders before they bid, so they know how much they'll make if they win. # This is probably a separate function

    def updateCurrentTopBid(self, newBid, newBidder):
        if newBid > self.currentTopBid:
            self.currentTopBid = newBid
            self.currentTopBidder = newBidder

            # oh wait bids are gonna need to be a class aren't they

    class Bid:
        bidder = models.Matchmaker() # does this need additional parameters? does it need to get models.Matchmaker, or...?
        bidAmount = models.DecimalField(max_digits = 5, decimal_places = 2, default = 0.00, validators = [MinValueValidator(0.01)])
        #marketClosureTime = definition

        def __init__(self, bidder, bidAmount, marketClosureTime):
            self.bidder = bidder
            self.bidAmount = bidAmount
            self.marketClosureTime = marketClosureTime

    def __str__(self):
        return self.idNum

'''











