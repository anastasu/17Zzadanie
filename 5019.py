f = open('17-281.txt')
s = f.readlines()
a = []
for i in s:
    a.append(int(i))
sum7 = 0
minsum = 10000
k = 0
for j in range(len(a)):
   sum7 = oct(j)[2:].count('7')  + sum7
for m in range(len(a)-1):
   if a[ m] > sum7 and a[m+1] > sum7:
     k += 1
     if a[ m] + a[m+1] < minsum:
       minsum = a[ m] + a[m+1]
print(k, minsum)