from django import forms
from .models import User, BookedFlight
from django.core.validators import EmailValidator

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100, validators=[EmailValidator()])
    password = forms.CharField(widget=forms.PasswordInput)

class FlightSearchForm(forms.Form):
    departure_place = forms.CharField(label='Departure Place')
    arrival_place = forms.CharField(label='Arrival Place')
    #departure_date = forms.DateField(label='Departure Date')

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookedFlight
        fields = ['user','flight_number','airline','departure_time','departure_place','destination']

class CancellingForm(forms.Form):
    user = forms.CharField(max_length=100)
    flight_number = forms.CharField(max_length=100)


 
