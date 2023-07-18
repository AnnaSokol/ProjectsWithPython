name = "mark mustermann"
print(name.title())
# Mark Mustermann

print(name.upper())
# MARK MUSTERMANN

print(name.lower())
# mark mustermann

print("hello string number1\nhello string number2")
# \n enter
# hello string number1
# hello string number2

print("Messages:\n\tMessage1\n\tMessage2\n\tMessage3\n")
# \t tab
# Messages:
# 	Message1
# 	Message2
# 	Message3

a = ".... Mark Mustermann ....."
print(a.rstrip())
print(a.lstrip())
print(a.strip())

a = ".... Mark Mustermann ....."
a = a.strip(".")
a = a.strip()
print(a)
# Mark Mustermann