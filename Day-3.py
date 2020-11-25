#First challenge
dic1 = {'a': 100, 'b': 200}
dic2 = {'x': 300, 'y': 200}
dic = dic1.copy()
dic.update(dic2)
print(dic)
#second challenge
dict={'a':20,'b':50,'c':100,'d':500}
del dict['c']
print(dict)
#third challenge
keys=['color:1','color:2','color:3','color:4']
colors=['red','blue','green','pink']
res = {}
for key in keys:
   for value in colors:
      res[key] = value
      colors.remove(value)
      break
print("Dictionary from lists :\n ",res)
#Fourth challenge
seta=set([12,1,0,13,14,15,1,61,70,500,1000])
print(len(seta))
#Fifth challenge
se1={1,4,7,8,5,2}
se2={3,6,9,8,5,1}
print("original sets:");
print(se1);
print(se2);
print("remove the intersection of a 2nd set from the 1st set using difference_update():");
se1.difference_update(se2)
print(se1);
se1={1,4,7,8,5,2}
se2={3,6,9,8,5,1}
print("Remove the intersection of a 2nd set from the 1st set using -= operator:");
print(se1-se2);
