from django.shortcuts import render, redirect

from .models import BookedFlight, User
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
import requests
from .aviation_stack import get_flight_info, search_flight
from .forms import FlightSearchForm, BookingForm, CancellingForm

# Create your views here.
""" def index(request):
    return render(request, "flights/index.html",{
        "flights": Flight.objects.all()
    }) """

def index(request):
    username = request.GET.get('username')
    if request.method == 'POST':
        #username = request.GET.get('username')
        form = FlightSearchForm(request.POST)
        API_KEY = "4dcedc037fdcf762cc197c60309f39ee" 
        if form.is_valid():
            departure_place = form.cleaned_data['departure_place']
            arrival_place = form.cleaned_data['arrival_place']
            #departure_date = form.cleaned_data['departure_date']

            # Perform flight search using the Aviation Stack API
            # Replace API_KEY with your Aviation Stack API key
            # Make API request to retrieve flight information
            # Example request: get_flight_info(departure_place, arrival_place, API_KEY)
            data = search_flight(API_KEY,departure_place,arrival_place) #departure_date)
            flight_results = data['data']

            # Pass the search results to the template for rendering
            # flight_results should be a list of flight objects with attributes like flight number and departure time
            
            form = FlightSearchForm()
            return render(request, 'icarus/index.html', {'flight_results': flight_results,
                                                  'form': form,'username':username})
    else:
        form = FlightSearchForm()

    return render(request, 'icarus/index.html', {'form': form,
                                                 'username':username})





""" def flight_details(request, flight_number):
    api_key = "4dcedc037fdcf762cc197c60309f39ee"  # Replace with your Aviation Stack API key
    data = get_flight_info(api_key, flight_number)
    try:
        #response = requests.get(url)
        #data = response.json()
        
        if 'error' in data:
            error_message = data['error']['info']
            return HttpResponse(f"Error retrieving flight details: {error_message}", status=400)
        
        # Extract relevant flight information from the data
        flight = {
            'flight_number': data['data'][0]['flight']['iata'],
            'airline': data['data'][0]['airline']['name'],
            'departure': data['data'][0]['departure']['airport'],
            'arrival': data['data'][0]['arrival']['airport'],
            'date': data['data'][0]['flight_date'],
            'status': data['data'][0]['flight_status'],
            # Add more flight details as needed
        }
        
        return render(request, 'flight_details.html', {'flight': flight})
    
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Error connecting to the API: {str(e)}", status=500)
    #return render(request, 'flight_details.html', {'flight': data})

 """

def book(request):
    username = request.GET.get('username')
    print(username)
    if request.method == "POST":
            form = BookingForm(request.POST)
            if form.is_valid():
            # Get the flight data from the form
                print('ok')
                print(form.cleaned_data)
               # form.save()
                user = form.cleaned_data['user']
                flight_number = form.cleaned_data['flight_number']
                airline = form.cleaned_data['airline']
                departure_time = form.cleaned_data['departure_time']
                departure_place = form.cleaned_data['departure_place']
                destination = form.cleaned_data['destination']

                # Create a new BookedFlight instance and save it to the database
                booked_flight = BookedFlight(
                    user = user,
                    #user= User.objects.get(username),  # Assuming you have authentication set up
                    flight_number=flight_number,
                    airline=airline,
                    departure_time=departure_time,
                    departure_place=departure_place,
                    destination=destination
                )
                booked_flight.save()


                return render(request, 'icarus/flight_details.html/',{'user':user,
                                                                     'flight_number':flight_number,
                                                                     'airline':airline,
                                                                     'departure_time':departure_time,
                                                                     'departure_place':departure_place,
                                                                     'destination':destination})
    else:
        form = FlightSearchForm()

    return render(request, 'icarus/index.html', {'form': form})

def booked_flights(request):
    # Get the current user's username
    username = request.GET.get('username')

    # Query the BookedFlight model for flights with the current username
    flights = BookedFlight.objects.filter(user=username)
    

    # Pass the flights to the booked.html template
    return render(request, 'icarus/booked.html', {'flights': flights,
                                                  'username': username})

def cancel_flights(request):
    username = request.GET.get('username')
    if request.method == "POST":
            form = CancellingForm(request.POST)
            if form.is_valid():
            # Get the flight data from the form
                print('ok')
                print(form.cleaned_data)
               # form.save()
                username = form.cleaned_data['user']
                flight_number = form.cleaned_data['flight_number']
                 # Retrieve the BookedFlight objects that match the provided name and flight number
                flights_to_cancel = BookedFlight.objects.filter(user=username, flight_number=flight_number)
                print('okay')

                # Delete the matched BookedFlight objects
                for flight in flights_to_cancel:
                    flight.delete()
                #flights.delete()
                flights = BookedFlight.objects.filter(user=username)

                # Pass the flights to the booked.html template
                return render(request, 'icarus/booked.html', {'flights': flights,
                                                            'username': username})
    flights = BookedFlight.objects.filter(user=username)
    # Redirect to a success page or another appropriate URL
    return render(request, 'icarus/booked.html',{'flights':flights,
                                                 'username':username})

            
""" 
            flight_date = form.cleaned_data['flight_date']
            flight_number = form.cleaned_data['flight_number']
            airline = form.cleaned_data['airline']
            departure_time = form.cleaned_data['departure_time']
            departure_place = form.cleaned_data['departure_place']
            destination = form.cleaned_data['destination']

            user = request.user
            flight_number = models.CharField(max_length=50)
            airline = models.CharField(max_length=100)
            departure_time = models.DateTimeField()
            departure_place = models.CharField(max_length=100)
            destination = models.CharField(max_length=100)
            return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
 """