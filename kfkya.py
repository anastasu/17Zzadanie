f = open('17-2.txt')
s = f.readlines()
a = []
for i in s:
    a.append(int(i))
k = 0
m = 0
for i in range(len(a)-1):
    if (a[i] * a[i+1]%3 == 0) and (a[i]+a[i+1])%2!=0:
        k+=1
        if (a[i]+a[i+1])>m:
            m=a[i]+a[i+1]
print(k, m)