mylist=[1,2,3]
mylist.append(5)  
print(mylist)

mylist.remove(2) #deletes an item
print(mylist)

max_list=max(mylist)
min_list=min(mylist)
print(max_list , min_list)      #max and min no. from list

age=(12,15,20,9)
rev_tuple=tuple(reversed(age))      #reversing tuple
print(rev_tuple)

fruits=("mango","orange","apple")
list_fruits=list(fruits)        #tuple to list conversion
print(list_fruits)
