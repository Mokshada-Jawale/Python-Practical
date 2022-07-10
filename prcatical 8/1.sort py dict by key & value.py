# Python program to sort the given dictionary by keys and values
from collections import OrderedDict
dict=eval(input("Enter a dictionary: "))
print("The dictionary in sorted order by keys is: ")
sorted_key=OrderedDict(sorted(dict.items()))
print(sorted_key)
print()
print("The dictionary in sorted order by values is: ")
sorted_val=sorted(dict.items(), key=lambda kv:(kv[1], kv[0]))
print(sorted_val)