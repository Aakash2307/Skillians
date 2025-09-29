a = [1,3,4,9,6,2,1]
n = len(a)
ans = n*[-1]

s = []
for i in range( n-1, -1,-1):
    while len(s)>0 and s[-1] < a[i]:
        s.pop()

    if len(s)>0:
        ans[i] = s[-1]

    else:
        ans[i] = -1

    s.append(a[i])


print (ans)