trip_dictionary = {
    'destination': ['Charlotte', 'Houston', 'New York City', 'Los Angeles'],
    'transportation': ['Tesla', 'Harley Davidson', 'Plane', 'Train'],
    'entertainment': ['Sporting Event', 'Music Festival', 'Art Gallery Tour', 'Hiking'],
    'dining': ['Best Burger', 'Pizza & Pasta', 'Tapas', 'Pho']
    }

import random

print('')
print(trip_dictionary)
#print(trip_dictionary['destination'])
print(random.choice(trip_dictionary['destination']))
print(random.choice(trip_dictionary['transportation']))
print(random.choice(trip_dictionary['entertainment']))
print(random.choice(trip_dictionary['dining']))