import requests

def get_flight_info(api_key, flight_number):
    url = f"http://api.aviationstack.com/v1/flights?access_key={api_key}&flight_iata={flight_number}"
    response = requests.get(url)
    data = response.json()
    return data

def search_flight(api_key, flight_iata, flight_arr):  # flight_date):
    url = f"http://api.aviationstack.com/v1/flights?access_key={api_key}&dep_iata={flight_iata}&arr_iata={flight_arr}" #&flight_date={flight_date}"
    response = requests.get(url)
    data = response.json()
    return data