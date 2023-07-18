cars = ['BMW', 'VW', 'Tesla', 'Toyota', 'Lexus']

for x in cars:
    print(x.upper())
    # BMW VW TESLA TOYOTA LEXUS
for x in range(1, 6):
    print(x)
    # 1 2 3 4 5

mynumber_list = list(range(0, 10))
# create new list with number
print(mynumber_list)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in mynumber_list:
    x = x * 2
    print(x)
    # 0 2 4 6 8 10 12 14 16 18

mynumber_list.sort(reverse=True)
print(mynumber_list)
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(str(max(mynumber_list)))
# 9

print(str(min(mynumber_list)))
# 0

print(str(sum(mynumber_list)))
# 45

#         0      1     2         3         4
cars = ['BMW', 'VW', 'Tesla', 'Toyota', 'Lexus']
myCars = cars[2:4]
print(myCars)
# new list ['Tesla', 'Toyota']

newCars = cars[:4]
print(newCars)
# new list without last car
# ['BMW', 'VW', 'Tesla', 'Toyota']

newCars = cars[-3:-1]
print(newCars)
# ['Tesla', 'Toyota']

copyCars = cars[:]
# variant 1 for copy, vom Anfang bis zum Ende

copy_cars = cars
# variant 2 for copy, die beide werden gleich