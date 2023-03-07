n=int(input())
list=[]
sum=[]
for i in range (1,n):
    a=int(input())
    list.append(a)
for i in range(1,n):
    sum.append(list[i-1]+list[i+1]+list[i])
a=max(sum)
print(a)