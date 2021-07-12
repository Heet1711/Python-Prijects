print ("Select the operation you want to perform")
print ("+")
print ("-")
print ("*")
print ("/")

operation = input("Choose the operation you want to perform : ")

if operation == '+':
    number1 = float(input("Number 1 : "))
    number2 = float(input("Number 2 : "))
    result = number1 + number2
    print("{0} + {1} = {2}".format(number1,number2,result)) 

elif operation == '-':
    number1 = float(input("Number 1 : "))
    number2 = float(input("Number 2 : "))
    result = number1 - number2
    print("{0} - {1} = {2}".format(number1,number2,result))

elif operation == '*':
    number1 = float(input("Number 1 : "))
    number2 = float(input("Number 2 : "))
    result = number1 * number2
    print("{0} * {1} = {2}".format(number1,number2,result))

elif operation == '/':
    number1 = float(input("Number 1 : "))
    number2 = float(input("Number 2 : "))
    if number2 == 0.0:
        print("Not Defined")
    else:
        result = number1 / number2
        print("{0} * {1} = {2}".format(number1,number2,result))

else:
    print ("Invalid")
