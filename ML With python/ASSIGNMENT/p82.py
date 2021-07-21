sentence=input("Plese enter the sentence : ")
s=sentence.split(" ")
word=input("Enter word that you want check : ")
if word in s:
 print("This word is available in this Sentence")
else:
 print("This word is not available in this sentence")