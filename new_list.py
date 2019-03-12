from math import sqrt
a=[2,4,9,16,25]
a1=[sqrt(i) for i in a]

a2=[]
for i in a:
    a2.append(sqrt(i))

def kvad(i):
    return sqrt(i)
a3=list(map(kvad,a))

print(a1)
print(a2)
print(a3)
