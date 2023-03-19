from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from . models import Flight, Passenger
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "flights/index.html",{
        "flights": Flight.objects.all()
    })

def flight(request,flight_id):
    flight = Flight.objects.get(pk=flight_id) #or pk for primary key 
    return render(request, "flights/flight.html",{
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all(), #passengers except the ones who are already on the flight - for our dropdown
        "passenger_count": flight.passengers.count()
    })

# def pass_count(request,flight_id):
#     flight = Flight.objects.get(pk=flight_id)
#     passenger_count = flight.passengers.count()
#     return render(request, {
#         "flight": flight,
#         "passenger_count": passenger_count
#     })

@staff_member_required
def book(request, flight_id):
    if request.method == "POST":
        try:
            flight = Flight.objects.get(pk=flight_id)
            passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
            passenger.flights.add(flight)
            return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
        except MultiValueDictKeyError:
            messages.warning(request, "No Passengers Left")
            return HttpResponseRedirect(reverse("flight", args=(flight_id,))) # redirect to same page with an error message
    else:
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))

@staff_member_required
def unbook_flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passenger_id = request.POST.get('passenger')
    if passenger_id:
        passenger = Passenger.objects.get(id=passenger_id)
        flight.passengers.remove(passenger)
    return redirect('flight', flight_id=flight_id)
