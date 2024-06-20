my_list=[1,2,3,4]
'''
List methods:
1.sort()
2.clear()
3.append()
4.count()
5.extend([4])
6.insert()
7.index()
8.len()
9.remove()
10.pop()
11.reverse()
12.copy()
13.max()
14.min()
15.del()
'''
mylist=[1,2,3,4,4,4,55,6]
mylist.sort()
print(mylist)
mylist.append(99)
print(mylist)
mylist.extend([44,77,88])
print(mylist)
#to count number of tym the element is present
print(mylist.count(4))
#insert 22 at index 1
mylist.insert(1,22)
print(mylist)
max=max(mylist)
print(max)
min=min(mylist)
print(min)
#deliting an element at index 2
del mylist[2]
print(mylist)
copylist=mylist.copy()
print("coppied list=",copylist)
copylist.reverse()
print("Reverselist=",copylist)

