from django.urls import path, include
#from .views import flight_details

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("<int:flight_id>", views.flight, name="flight"),
    path("book", views.book, name="book"),
    #path('flight/<str:flight_number>/', flight_details, name='flight_details'),
    path("booked_flights", views.booked_flights, name="booked_flights"),
    path("cancel_flights", views.cancel_flights, name="cancel_flights"),
    #path('users/', include(('users.urls', 'users'), namespace='users')),
    #path('', views.flight_search, name='flight_search')
]
