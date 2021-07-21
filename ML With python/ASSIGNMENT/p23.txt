s=int(input("Enter th baxic salary"))
if s>=1 and s<=4000:
 hra=(s*10)/100
 da=(s*50)/100
 print("Gross salary  : ",s+hra+da)
elif s>=4001 and s<=8000:
 hra=(s*20)/100
 da=(s*60)/100
 print("Gross salary  : ",s+hra+da)
elif s>=8001 and s<=12000:
 hra=(s*25)/100
 da=(s*70)/100
 print("Gross salary  : ",s+hra+da)
elif s>12000:
 hra=(s*30)/100
 da=(s*80)/100
 print("Gross salary  : ",s+hra+da)