def addfraction(f1,f2):
    denom=f1[1]*f2[1]
    num=(f1[0]*f2[1])+(f2[0]*f1[1])
    return (num,denom)

f1=(1,2)
f2=(2,3)
print(addfraction(f1,f2))

