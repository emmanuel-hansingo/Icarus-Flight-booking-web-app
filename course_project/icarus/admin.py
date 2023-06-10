from django.contrib import admin

from .models import User ,BookedFlight  #, Flight, Passenger

""" admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger) """
admin.site.register(User) 
admin.site.register(BookedFlight)