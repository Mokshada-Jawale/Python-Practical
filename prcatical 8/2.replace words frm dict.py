# Python program to replace values from the dictionary
dict=eval(input("Enter a dictionary: "))
print("The entered dictionary is: \n",dict)
key=eval(input("Enter the key whose value you want to replace: "))
val=eval(input("Enter the new value for the entered key: "))
dict[key]=val
print("The updated dictionary is: ",dict)