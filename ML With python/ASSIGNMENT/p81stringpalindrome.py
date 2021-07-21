
string=input("Plese Enter a string : ")
print(string)
rstring="".join(reversed(string))
print(rstring)
if string==rstring:
 print("String is Palindrome")
else:
 print("string not palidrom")