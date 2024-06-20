#def add(a,b):
    #c=a+b
    #return c

#print("sum of",add(10,20))
def remove_duplicate(li):
    unique_list = []
    duplicate_list = []

    for i in li:
        if i not in unique_list:
            unique_list.append(i)
        else:
            duplicate_list.append(i)

    return unique_list


li = [1, 2, 3, 5, 7, 3, 2, 1]
print("Original list:", li)
print("List after removing duplicates:", remove_duplicate(li))


