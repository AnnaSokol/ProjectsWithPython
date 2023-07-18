for x in range(0, 100 + 1):
    print(x)

for y in range(10, 100, 2):
    print("Number y = " + str(y))
    if y == 88:
        break

print("------EOF-----")
# print gerade Zahlen
# (start, end, step)

i = 0
while True:
    print(i)
    i=i+1
    if i == 100:
        break