s="aabb"
res=""
c=1
n=len(s)
for i in range(1,n):
    if s[i-1]==s[i]:
        c=c+1

    else:
       res=res+s[i-1]
       if c > 1:
            res += str(c)
       c = 1
res = res + s[-1]
if c > 1:
         res += str(c)
print(res)

