#program to remove ith occurance of a given word in a list where words repeat
def Remove_Word(list, word, N):
    newList = []
    count = 0

    for i in list:
        if (i == word):
            count = count + 1
            if (count != N):
                newList.append(i)
        else:
            newList.append(i)
    list = newList

    if count == 0:
        print("Item not found")
    else:
        print("Updated list is: ", list)
    return newList

list = ['This','is','mokshada','this','is','Mokshada']
word = 'this'
N = 1

Remove_Word(list, word, N)