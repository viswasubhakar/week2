# question 1
data = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
sorted_data = sorted(data, key=lambda x: x[1])
for item in sorted_data:
    print(item)

    
# question 2
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1=list(map(lambda x:x*x ,l))
print(l1)


# question 3
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1=tuple(map(lambda x:str(x) ,l))
print(l1)


# question 4
from functools import reduce
l=[]
for i in range(1,26):
    l.append(i)
prod=reduce(lambda x,y:x*y ,l)
print (prod)


# question 5
l=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
l1=filter(lambda x:x if x%2==0 and x%3==0 else 0,l)
print(list(l1))

# question 6
strs=['python', 'php', 'aba', 'radar', 'level']
palendromes=filter(lambda a:a if a==a[::-1] else 0,strs)
print(list(palendromes))


