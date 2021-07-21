class Bank:
 def interest(self):
  print("Bank interest is : 0")
class Sbi(Bank):
 def interest(self):
  print("SBI interest is : 3.50%-5.70%")
class Pnb(Bank):
 def interest(self):
  print("PNB interest is : 7.20%–8.00%")
b=Bank()
b.interest()
p=Pnb()
p.interest()
s=Sbi()
s.interest()