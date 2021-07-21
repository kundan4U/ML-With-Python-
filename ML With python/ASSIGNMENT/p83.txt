sentence=input("plese Enter the sentence sentence :")
word=input("Enter word that you want Occurrence   :")
a=[]
count=0
a=sentence.split(" ")
for i in range(0,len(a)):
      if(word==a[i]):
            count=count+1
print("Occurence of the word is : ",count)
