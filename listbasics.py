mynegh=[36,37,38]

#appending and inserting values
mynegh.append(39)
mynegh.append(40)
mynegh.append(41)
mynegh.insert(0,33)
mynegh.insert(1,34)
mynegh.insert(1,35)

print(mynegh)

#pop remove del 

mynegh.pop(0)
print(mynegh)

mynegh.remove(41)
print(mynegh)

del mynegh[-1]
print(mynegh)

#copying values and creating new list

mynegh2=mynegh#this both will have same memory location
print(mynegh)

#these both have different memory location
myneghlist=list(mynegh)
print(mynegh)

myneghcopy=mynegh.copy()
print(mynegh)

#sort and reverse
mynegh.sort(reverse=True)#reversing
print(mynegh)

mynegh.reverse()#reversing again and getting original
print(mynegh)

#clearing a list-empty list
myneghlist.clear()
print(myneghlist)
print(mynegh)








