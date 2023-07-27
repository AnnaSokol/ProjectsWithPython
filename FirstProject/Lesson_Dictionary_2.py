apartment = {
    'location': 'Berlin',
    'room': 2,
    'space': 65,
    'price': 800
}
all_apartment = []
for x in range(0, 10):
    all_apartment.append(apartment.copy())

for wohnung in all_apartment:
    print(wohnung)
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800}
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800}
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800}
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800}
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800}
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800}
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800}
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800}
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800}
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800}
print("----------------------")
all_apartment[5] ['room'] = 3
for wohnung in all_apartment:
    print(wohnung)
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800}
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800}
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800}
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800}
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800}
# {'location': 'Berlin', 'room': 3, 'space': 65, 'price': 800}
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800}
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800}
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800}
# {'location': 'Berlin', 'room': 2, 'space': 65, 'price': 800}
