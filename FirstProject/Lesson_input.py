name = input("Please enter Your name")
print("Hello "+ name)

nr1 = input("Enter X: ")
nr2 = input("Enter Y: ")
nr3 = int(nr1) + int(nr2)
print(nr3)
# Please enter Your nameAnna
# Hello Anna
# Enter X: 5
# Enter Y: 9
# 14

message = ""
while True:
    message = input("Enter password")
    if message == 'secret': break
    print(message + "Password Not Correct")
#---------------------------------------------------

myList = []
msg = ""
while msg != 'stop':
    msg = input("Enter new item, and STOP to finish")
    myList.append(msg)

print(myList)
# Enter new item, and STOP to finishKonrad
# Enter new item, and STOP to finishNicoly
# Enter new item, and STOP to finishMarkus
# Enter new item, and STOP to finishOlga
# Enter new item, and STOP to finishTom
# Enter new item, and STOP to finishstop
# ['Konrad', 'Nicoly', 'Markus', 'Olga', 'Tom', 'stop']