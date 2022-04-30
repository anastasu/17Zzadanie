f = open ('17-278(2).txt')
d=[]
while True:
    s = f.readline()
    if s == ''
        break
    d.append(int(s))
smax = 0
cnt = 0
max_sum = 0
for i in range(len(d)):
    if d[i] % 32 == 0:
        s = ''
        while d[i]>0:
            s = str (d[i]%5)+s
            d[i] // 5
        smax += s.count('3')*3
for i in range (len(d)-2) :
    if (d[i]>smax) or d[i+1] > smax or d[i+2] >smax:
        cnt+=1
        max_sum = max(max_sum, d[i])+ d[i+1]+ d[i+2])
print (cnt, max_)