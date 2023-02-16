s="aabbccdd"
res=""
c=0
n=s(len)
for i in range(1,n):
    if s[i-1]==s[i]:
        c=c+1
        i=i+1
    else:
        res=res+str(c)+str[i]
print(res)
        

