d={}

with open('nyc_weather.csv','r') as f:
    f.readline()

    for line in f.readlines():
        k,l=line.split(',')
        l=int(l)
        d[k]=l

    print(d)

print('temp on jan 9:',d['Jan 9'])
print('temp on jan 4:',d['Jan 4'])


