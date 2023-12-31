from django.db import models
from datetime import date

# Genders are assigned prime numbers, and orientations are assigned composite numbers
# compareOrienders works, at least in shell
def compareOrienders(alice, bob):
    return (((bob.orientation % alice.gender) == 0) and ((alice.orientation % bob.gender) == 0))
    
def compareAges(alice, bob):
    return ((alice.age >= bob.minAge) and (alice.age <= bob.maxAge) and (bob.age >= alice.minAge) and (bob.age <= alice.maxAge))

def calculateAge(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

# Will require fiddling with coordinates and map APIs ktl.

'''
def getDistance(lat1, lon1, lat2, lon2):
    distance = 20 # placeholder	
    return distance

def compareLocations(alice, bob):
    aliceBobDistance = getDistance(alice.homeLatitude, alice.homeLongitude, bob.homeLatitude, bob.homeLongitude)
    return (aliceBobDistance <= alice.maxDistance and aliceBobDistance <= bob.maxDistance)
'''