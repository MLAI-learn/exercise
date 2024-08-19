with open('nyc_weather.csv','r') as f:
    l=[]
    k=f.readline()

    for line in f.readlines():
        d,t=line.split(',')
        try:
            h=float(t)
            

        except Exception as e:
            pass
        finally:
            l.append(h)

    print(l)
    

    avg_temp= sum(l[0:7])/len(l[0:7])
    print('avg temp:',avg_temp)

   
    print('maximum temp:',max(l[0:10]))    


    