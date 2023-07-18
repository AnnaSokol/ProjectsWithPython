age = 8

if(age <= 4):
    print("You are baby")
elif (age > 4) and (age < 12):
    print("you are kid")
elif (age >= 12) and (age < 19):
    print("You are teenager")
else:
    print("you are old")
#------------------------------------------------

all_fruit = ['banana', 'apple', 'abricot', 'orange', 'papaya', 'peach', 'rambutan']
myFruit = ['banana', 'apple', 'orange']

if 'banana' in all_fruit:
    print("yes Banana is in the list")
else:
    print("'banana' is not in the list")
#---------------------------------------

for x in all_fruit:
    if x in myFruit:
        print( x + " is my favorite fruit")
    else:
        print( x + " is not my fruit")
# banana is my favorite fruit
# apple is my favorite fruit
# abricot is not my fruit
# orange is my favorite fruit
# papaya is not my fruit
# peach is not my fruit
# rambutan is not my fruit