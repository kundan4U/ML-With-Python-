f=None
try:
 filename=input("Enter the file name to read")
 f=open(filename,"r")
 content=f.read()
 print(content)
 
except FileNotFoundError:
 print("File does not exists")
finally:
 if f:
  f.close()
  print("File is close")