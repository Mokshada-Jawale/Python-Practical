#python program to count occurences of given word in a sentence
from collections import Counter
s=input("Enter a string: ")
l=list(map(str, s.split(" ")))
key=input("Enter the word to count its occurences: ")
d=Counter(l)
print("Number of occurences of",key, "in the given sentence are: ",d[key])
