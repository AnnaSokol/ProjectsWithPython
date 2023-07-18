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