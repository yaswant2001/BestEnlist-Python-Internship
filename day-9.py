#First challenge
def challengefunction(k):
    return lambda a:a*k
multi=challengefunction(10)
print(multi(50));
#secondchallenge
def fibonacci(count): 
    fib_list = [0, 1] 
  
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])), 
                                         range(2, count))) 
  
    return fib_list[:count] 
  
print(fibonacci(5));
#thirdchallenge
mylist=[5,2,8,7,9,15]
n=3
print("The list: ",mylist);
print("Multiplied number: ",n);
filtered_numbers=list(map(lambda number:number*n,mylist))
print("result: ");
print(' '.join(map(str,filtered_numbers)));
#fourthchallenge
mylist=[15,10,25,14,2,3,6,9]
result=list(filter(lambda x: (x%9==0),mylist))
print("Numbers divisible by 9 are",result)
#fifthchallenge
list1 = [21,3,4,6,33,2,3,1,3,76]
odd_count = len(list(filter(lambda x: (x%2 != 0) , list1)))
even_count = len(list(filter(lambda x: (x%2 == 0) , list1)))
print("Even numbers available in the list: ", even_count)
print("Odd numbers available in the list: ", odd_count)
