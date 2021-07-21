try:
 x=int(input("Plese enter the first number   :"))
 y=int(input("Plese enter the  second number :"))
 z=x/y
 print("division is :",z)
except ZeroDivisionError:
 print("Plese dont enter Zero")
finally:
 print("Good bye")