vow=['a','e','i','o','u','A','E','I','O','U']
n=list(input())[::-1]
k=[]
for i in n:
    if i not in vow:
        k.append(i)
print("".join(str(x) for x in (k)))
