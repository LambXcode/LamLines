from django.contrib import admin
from .models import Flight,Airport,Passenger

# Register your models here.

class FlightAdmin(admin.ModelAdmin):   #lets see more info of a flight 
    list_display = ("id","origin","destination","duration")

class PassengerAdmin(admin.ModelAdmin): #lets see more info of a passenger
    filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
admin.site.site_url = '/users/login'
