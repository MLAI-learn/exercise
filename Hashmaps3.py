p={}

with open('poem.txt','r') as f:
    for line in f.readlines():
        t=line.split(' ')
        t[-1]=t[-1][:-1]
        for k in t:
            
            if k in p:
                p[k]+=1
            else:
                p[k]=1
            
print(p)
    
