trip_dictionary = {
    'destination': ['Charlotte', 'Houston', 'New York City', 'Los Angeles'],
    'transportation': ['Tesla', 'Harley Davidson', 'Plane', 'Train'],
    'entertainment': ['Sporting Event', 'Music Festival', 'Art Gallery Tour', 'Hike'],
    'dining': ['Best Burger', 'Pizza & Pasta', 'Tapas & Tequila', 'Pho Real']
    }

import random


print('')

print('')


user_name = input('Name: ')
txt = 'Welcome to Your Trip Generator, {}!'
print('')
print(txt.format(user_name)) 
print('')
print('Lets choose your destination.')
print('')

user_dictionary = {
'destination': (random.choice(trip_dictionary['destination'])),
'transportation': (random.choice(trip_dictionary['transportation'])),
'entertainment': (random.choice(trip_dictionary['entertainment'])),
'dining': (random.choice(trip_dictionary['dining']))
}
#print(user_dictionary)
random_destination = (random.choice(trip_dictionary['destination']))
random_transportation = (random.choice(trip_dictionary['transportation']))
random_entertainment = (random.choice(trip_dictionary['entertainment']))
random_dining = (random.choice(trip_dictionary['dining']))

new_random_destination = (random.choice(trip_dictionary['destination']))
new_random_transportation = (random.choice(trip_dictionary['transportation']))
new_random_entertainment = (random.choice(trip_dictionary['entertainment']))
new_random_dining = (random.choice(trip_dictionary['dining']))

txt = 'Does'+(' ')+(random_destination)+(' ')+'work for you? Y/N '
user_destination = input(txt)
yes_choice = ['yes','y','Y','Yes']
while user_destination not in yes_choice:
    txt = 'Does'+(' ')+(new_random_destination)+(' ')+'work instead? Y/N '
    user_destination = input(txt) 
if user_destination in yes_choice:
    txt = 'Great! Your destination is {}!'
    print(txt.format(random_destination))   
elif user_destination in yes_choice:
    txt = 'Great! Your destination is {}!'
    print(txt.format(new_random_destination))    

print('')
print('Lets choose your transportation.')
print('')

txt = 'Does'+(' ')+(random_transportation)+(' ')+'work for you? Y/N '
user_transportation = input(txt)
yes_choice = ['yes','y','Y','Yes']
while user_transportation not in yes_choice:
    txt = 'Does'+(' ')+(new_random_transportation)+(' ')+'work instead? Y/N '
    user_transportation = input(txt) 
if user_transportation not in yes_choice:
    txt = 'Does'+(' ')+(new_random_transportation)+(' ')+'work instead? Y/N '
    user_transportation = input(txt)     
if user_transportation in yes_choice:
    txt = 'Great! You will be traveling via {}!'
    print(txt.format(random_transportation))    
elif user_transportation in yes_choice:
    txt = 'Great! You will be traveling via {}!'
    print(txt.format(new_random_transportation))    

print('')
print('Lets choose your entertainment.')
print('')

txt = 'Does'+(' ')+(random_entertainment)+(' ')+'work for you? Y/N '
user_entertainment = input(txt)
yes_choice = ['yes','y','Y','Yes']
while user_entertainment not in yes_choice:
    txt = 'Does'+(' ')+(new_random_entertainment)+(' ')+'work instead? Y/N '
    user_entertainment = input(txt) 
if user_entertainment in yes_choice:
    txt = 'Great! You will be enjoying a {}!'
    print(txt.format(random_entertainment))    
elif user_entertainment in yes_choice:
    txt = 'Great! You will be enjoying a {}!'
    print(txt.format(new_random_entertainment)) 

print('')
print('Lets choose your dining.')
print('')

txt = 'Does'+(' ')+(random_dining)+(' ')+'work for you? Y/N '
user_dining = input(txt)
yes_choice = ['yes','y','Y','Yes']
while user_dining not in yes_choice:
    txt = 'Does'+(' ')+(new_random_dining)+(' ')+'work instead? Y/N '
    user_dining = input(txt) 
if user_dining in yes_choice:
    txt = 'Great! You will be dining at {}!'
    print(txt.format(random_dining))    
elif user_dining in yes_choice:
    txt = 'Great! You will be dining at {}!'
    print(txt.format(new_random_dining))    

print('')
print('Lets finalize your trip.')
print('')    

txt = '{}, you will be traveling to {} via {}. While there, you will enjoy a {} followed by dining at {}.'
trip_summary = [user_name,random_destination,random_transportation,random_entertainment,random_dining]
print (txt.format(user_name,random_destination,random_transportation,random_entertainment,random_dining))

print('')
user_finalize = input('Are you ready to finalize trip? Y/N ')
print('') 
print('Fantastic! Trip Generator')