#List
List1 = ['Anshika',21,14.55,'A']

print(List1)
print(List1[0])
print(List1[1])

print(List1[-1])
print(List1[-2])

print('lenght of list =',len(List1))

List2 = ['Anshi',22,14.55,'B']

List = List1+List2
print(List)

Mul_List = List1*2
print(Mul_List)

List3 = List2[2:3]
List4 = List2[1:3]

print(List3)
print(List4)

l1 = [1,2,3,'A','B']

del l1[1]
del l1[3]
print(l1)

l2 = [1,3,5,7,9,3,5,3,3]

l2.append([25,30])
print("after append =",l2) #we can add more element in a list by using append() method

print("element 3 is occured :", l2.count(3)) #count() method counts how many times an element has occured in a list

print("index of 5 =", l2.index(5)) #index()method finds the given element in a list

l3 = [20,40,60,80,100]
l3.insert(0,10) #insert method insert a element to the list in a given index
print(l3)

l3.insert(3,50)
print(l3)

l4 = ['a','b','c','d','e']
l4.reverse()
print(l4)

l4.reverse()
l4.remove('c')
print(l4)

l5 = ['anshi', 'ansh', 'anshika', 'shrivansh']
l5.pop(2) #pop()method is another name of remove()method
print('After pop method list is =', l5)

print('sorted list :', l5.sort())

l6 = [2, 3, 5, 7, 9, 3, 5, 3, 3]
print('max value of l6 =',max(l6))
print('min value of l6 =',min(l6))

l7 = ['anshi', 'ansh', 'anshika', 'shrivansh']
print('max value of l7 =',max(l7))
print('min value of l7 =',min(l7))

tuple = (11,14,17,20,25)
print(list(tuple)) #list() method converts tuple into list

del l7 #show error because we delete the L7 that's why it shows a L7 is not defined
print(l7)