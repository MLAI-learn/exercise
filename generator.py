def square():
    a=1
    while True:
        yield  a*a
        a+=1
        
        

for s in square():
    while s>100:
        break
    else:
        print(s)