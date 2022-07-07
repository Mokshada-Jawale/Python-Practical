from collections import Counter
s=input("Enter a string: ")
l=list(map(str, s.split(" ")))
d=Counter(l)
print(d)
print("Number of occurences of each word in the given sentence are: ")
for i in d:
    print(i,d[i],sep=': ')
