import math
import os
import random
import re
import sys

n=int(input("Plese enter any number"))
if n%2==1:
 print("Weired")
elif n%2==0 and n>=2 and n<=5:
 print("Not Weired")
elif n%2==0 and n>=6 and n<=20:
 print("Weired")
elif n%2==0 and n>20:
 print("Not Weired")