def div(x,y):
 try:
  result=x/y
 except ZeroDivisionError:
  print("Are you typint /Zero ")
 else:
  print("Result=",result)
 finally:
  print("This is the final block")
a=int(input("Enter first no :"))
b=int(input("Enter Second no :"))
div(a,b)