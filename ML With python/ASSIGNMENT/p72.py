try:
 x=int(input("Enter first number"))
 y=int(input("Enter Second number"))
 print("Division is : ",x/y)
except ZeroDivisionError:
 print("Plese dont use /Zero")
finally:
 print("Good Bye,,,See You Again,,,,.....")