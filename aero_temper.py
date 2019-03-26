with open('temp.txt','r') as file:
    content=file.read()
a=content.split()
h=0
for i in range(len(a)):
    a[i]=float(a[i])
for i in a:
    if a.count(i)==1:
        h+=1
print("Максимальная =", max(a),
      "\nМинимальная =", min(a),
      "\nСредняя =",round(sum(a)/len(a),2),
      "\nУникальных =",h)
