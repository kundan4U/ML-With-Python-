try:
 x=int(input("Enter first number"))
 y=int(input("Enter Second number"))
 print("Division is : ",x/y)
except ValueError:
 print("Plese dont use other value except integer")
finally:
 print("Good Bye,,,See You Again,,,,.....")