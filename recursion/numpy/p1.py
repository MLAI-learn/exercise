import numpy as np

# Employee Details (1) Employee ID (2) Department (3) Salary
ed = np.array([
    [101, 'Sales', 55000, 'Satya Nadella'],  
    [102, 'HR', 52000, 'Emily Johnson'],    
    [103, 'IT', 72000, 'Fatima Razaak'],        
    [104, 'Sales', 60000, 'John Smith'],    
    [105, 'IT', 68000, 'Priya Singh'],      
    [106, 'HR', 54000, 'Li Wei'],           
    [107, 'IT', 71000, 'Michael Brown'],    
    [108, 'Sales', 59000, 'Sunita Sharma'], 
    [109, 'HR', 53000, 'Chen Wei']          
])

# Performance Metrics (1) Employee ID (2) Performance Score (out of 100) (3) Number of Projects Completed
p_m = np.array([
    [101, 85, 5],
    [102, 78, 3],
    [103, 92, 7],
    [104, 88, 6],
    [105, 79, 4],
    [106, 81, 5],
    [107, 91, 8],
    [108, 77, 4],
    [109, 83, 4]
])

m=np.hstack((ed,p_m))
print(m)
print('salaries:',ed[:,2])
a=ed[:,2]
print(np.sort(a,axis=None))

for row in ed:
    print(f"Employee id: {row[0]} and Name: {row[3]}")

print(p_m[:,1])
p=p_m[:,1]
f=p.astype(float)
print(f)
av=f.mean()
print('avg:',av)
d=ed[:,1]
u=np.unique(d)
print(u)
avg_hr=ed[ed[:,1]=='HR',2]
print(avg_hr)
hr=avg_hr.astype(float)
print(hr.mean())