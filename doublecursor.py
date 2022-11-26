a=[1,2,3,5,5,5]
b=[4,6,9,10,10,10]

n,m=len(a),len(b)

i=j=0
c=[]
while i<n and j<m:
    if a[i]<b[j]:
        if a[i] in c:
            i+=1
            continue
        c.append(a[i])
        i+=1
    else:
        if b[j] in c:
            j+=1
            continue
        c.append(b[j])
        j+=1

while j<m:
    if b[j] in c:
        j += 1
        continue
    c.append(b[j])
    j+=1
while i<n:
    if a[i] in c:
        i += 1
        continue
    c.append(a[i])
    i+=1



# Удваивает значение
def double(x):
    return x*2
# Утраивает значение
def triple(x):
    return x*3