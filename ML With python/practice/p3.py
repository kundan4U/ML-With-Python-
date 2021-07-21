#calculater using function

def add():
 n1=eval(input("plese enter first nuber"))
 n2=eval(input("plese enter second number"))
 print("Sum is :",n1+n2)
def sub():
 n1=eval(input("plese enter first nuber"))
 n2=eval(input("plese enter second number"))
 print("Sub is :",n1-n2)
def mul():
 n1=eval(input("plese enter first nuber"))
 n2=eval(input("plese enter second number"))
 print("mul is :",n1*n2)
def div():
 n1=eval(input("plese enter first nuber"))
 n2=eval(input("plese enter second number"))
 print("div is :",n1/n2)
print("plese select option: 1=ADD 2=SUM 3=MUL 4=DIV")
n=int(input())
if n==1:
 add()
elif n==2:
 sub()
elif n==3:
 mul()
elif n==4:
 div()
else: 
 print("print enter correct NO :")
print("Thank You")


