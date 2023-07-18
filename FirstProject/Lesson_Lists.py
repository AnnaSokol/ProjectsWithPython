cities = ['New York', 'Moscow', 'new dehli', 'Berlin', 'Toronto']

print(cities)
# alle

print(len(cities))
# wie viel = 5

print(cities[0])
# print first City

print(cities[-1])
# print last city

print(cities[2].title())
# new dehli => New Dehli

cities[2] = 'Amsterdam'
print(cities)
# change city 'new dehli' to 'Amsterdam'
# ['New York', 'Moscow', 'Amsterdam', 'Berlin', 'Toronto']

cities.append('Barcelona')
print(cities)
# add new City 'Barcelona'

cities.insert(2, 'Hamburg')
# add new city 'Hamburg' betweem 'Moscow' and 'Amsterdam'

del cities[-1]
# delete last City

cities.remove('Moscow')
# delete city 'Moscow'

deleted_city = cities.pop()
# delete last city

cities.sort()
print(cities)
# sort alphabetisch ['Amsterdam', 'Berlin', 'Hamburg', 'New York']

cities.sort(reverse=True)
print(cities)
# ['New York', 'Hamburg', 'Berlin', 'Amsterdam']

cities.reverse()
print(cities)
# ['Amsterdam', 'Berlin', 'Hamburg', 'New York']
