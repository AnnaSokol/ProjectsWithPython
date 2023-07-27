def func_A():
    """Print text"""
    print("text text text text text text")
    print("Hello Hello Hello Hello Hello")

def func_B():
    """Print more text"""
    print("more text more text more text")

#--------------------------------------------------
func_A()
func_B()
def summa(x , y):
    return x + y

z = summa(2, 3)
print(z)
#--------------Factor-------------
# 2! = 1*2
# 3! = 1*2*3
# 4! = 1*2*3*4

def factorial(x):
    """calculate factorial of number X"""
    antwort = 1
    for i in range(1, x + 1):
        antwort = antwort * i
    return antwort

print(factorial(3))
#----------------------------------

for i in range(1,10):
    print(str(i) + "!\t= " + str(factorial(i)))
# 1!	= 1
# 2!	= 2
# 3!	= 6
# 4!	= 24
# 5!	= 120
# 6!	= 720
# 7!	= 5040
# 8!	= 40320
# 9!	= 362880