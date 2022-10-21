from flight_search import *
from data_manager import *
# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the
# program requirements.

c = {
  'prices': [
    {
      'city': 'Paris',
      'iataCode': 'CDG',
      'lowestPrice': 54,
      'id': 2
    },
    {
      'city': 'Berlin',
      'iataCode': 'BER',
      'lowestPrice': 42,
      'id': 3
    },
    {
      'city': 'Tokyo',
      'iataCode': 'HND',
      'lowestPrice': 485,
      'id': 4
    },
    {
      'city': 'Sydney',
      'iataCode': 'SYD',
      'lowestPrice': 551,
      'id': 5
    },
    {
      'city': 'Istanbul',
      'iataCode': 'IST',
      'lowestPrice': 95,
      'id': 6
    },
    {
      'city': 'Kuala Lumpur',
      'iataCode': 'KUL',
      'lowestPrice': 414,
      'id': 7
    },
    {
      'city': 'New York',
      'iataCode': 'LGA',
      'lowestPrice': 240,
      'id': 8
    },
    {
      'city': 'San Francisco',
      'iataCode': 'SFO',
      'lowestPrice': 260,
      'id': 9
    },
    {
      'city': 'Cape Town',
      'iataCode': 'CPT',
      'lowestPrice': 378,
      'id': 10
    }
  ]
}
c = c["prices"]
for city in c:
    a = FlightSearch("DMM", city["iataCode"], "21/10/2022", "1/11/2022", int(city["lowestPrice"]))
    a.search_flight()
