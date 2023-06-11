# question 1
def odd(l):
    l1=[]
    for i in l:
        if i%2!=0:
            l1.append(i)
    return l1
l=[]
for i in range(1,26):
    l.append(i)
print(odd(l))


# question 2
def fun(*args):
    return sum(args)
print(fun(1,2,3))

def fun1(**kargs):
    return kargs
print(fun1(a=1,b=2,c=3))



# question 3
num=[2, 4, 6, 8, 10, 12, 14,16, 18, 20]
num_itter=iter(num)
for i in range(0,5):
    print(next(num_itter))
    
    
    
    
# question 4
def fun():
    yield 1           
    yield 2           
    yield 3           
for value in fun():
    print(value)
    
    
# question 5
l=[]
for num in range(2,1001):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                break
        else:
            l.append(num)
    else:
        print(num, "is not a prime number")
def fun(l):
        for i in range(0,20):
            yield l[i]
for i in fun(l):
    print(i)
    

    
    
    
# question 6
count=0
a,b=0,1
while(count<10):
    print(a)
    sum=a+b
    a=b
    b=sum
    count=count+1

    
# question 7
str="pwskills"
newstr=iter(str)
print(list(newstr))


# question 8
number=121
s=str(number)
sr=s[::-1]
while(s==sr):
    print("its a palendrome")
    break
else:
    print("not a palendrome")
    
    
    



