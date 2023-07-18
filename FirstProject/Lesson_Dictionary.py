#   (-------Item-------)
#     (key)      (value
apartment = {
    'location': 'Berlin',
    'room': 2,
    'space': 65,
    'price': 800
}
print(apartment)
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800}

print("Location X = " + str(apartment['location']))
# Location X = Berlin

apartment['balcony'] = 'yes'
print(apartment)
# add new 'key' and 'value'
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800, 'balcony': 'yes'}

# del apartment['price']
# print(apartment)
# {'location': 'Berlin', 'room': 2, 'space': 65, 'balcony': 'yes'}
# delete key

apartment['location'] = apartment['location'] + 'Hamburg'
apartment['room'] = apartment['room'] + 1
if apartment['room'] == 3:
    apartment['price'] = apartment['price'] + 300
print(apartment)
# {'location': 'BerlinHamburg', 'room': 3, 'space': 65, 'price': 1100, 'balcony': 'yes'}

print(apartment.keys())
# dict_keys(['location', 'room', 'space', 'price', 'balcony'])

print(apartment.values())
# dict_values(['BerlinHamburg', 3, 65, 1100, 'yes'])