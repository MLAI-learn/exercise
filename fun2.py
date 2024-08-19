def print_(a=5):
    for i in range(a):
        s = ''
        for j in range(i+1):
            s = s + '*'
        print(s)
       


print_(10)
