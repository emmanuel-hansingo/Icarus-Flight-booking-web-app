from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import EmailValidator



# Create your models here.
""" class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    
    def __str__(self) :
        return f"{self.id}: {self.origin} to {self.destination}"
     """
    
class User(models.Model):
    username = models.CharField(max_length=64)
    email = models.EmailField(max_length=100, unique=True, validators=[EmailValidator()])
    password = models.CharField(max_length=64)


    def __str__(self):
        return f"{self.username} : {self.email}"
    
class BookedFlight(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    flight_number = models.CharField(max_length=50)
    airline = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    departure_place = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user} - Flight {self.flight_number}"


