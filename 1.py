num1={0}
num2={0}

n=int(input())
m=int(input())
for i in range(1,n):
    num1.add(int(input("1: ")))
    for j in range(1,m):
        num2.add(int(input("2: ")))
i=num1.intersection(num2)
i.remove(0)
print(i)