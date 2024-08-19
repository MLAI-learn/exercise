with open('student_marks.csv','r') as f:
    d={}
    keys=f.readline()
    keys=keys.split(',')
    keys[-1]=keys[-1][:-1]

    for key in keys:
        d[key]=[]

    for line in f.readlines():
        data=line.split(',')
        data[-1]=data[-1][:-1]

        j=0
        for key in d:
            d[key].append(data[j])
            j+=1

        
        
        
    d['total_marks']=[0]*5
    all_subjects=['Maths', 'Physics', 'Chemistry', 'English', 'Biology', 'Economics', 'History', 'Civics']
    for i in range(0,5):
        sum_=0
        for subject in all_subjects:
            try:
                sum_=sum_+int(d[subject][i])
            except:
                pass
        d['total_marks'][i]=sum_

    d['avg marks']=[0]*5
    total_subjects=len(all_subjects)
    for i in range(5):
        d['avg marks'][i]=d['total_marks'][i]/total_subjects

    f_out=open('output.csv','w')
    header=','.join(key for key in d.keys())
    f_out.write(header+'\n')


    for key in d:
        value=','.join(str(v) for v in d[key])
        f_out.write(value+'\n')

f_out.close()



with open('output.csv','r') as f:
    print(f.read())





     
