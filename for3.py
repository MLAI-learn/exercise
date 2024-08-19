e= [2340, 2500, 2100, 3100, 2980]
m=['jan','feb','mar','april','may']
a=input('enter amount')
A = int(a)

month=-1
for i in range(len(e)):
    if A==e[i]:
        month=i
        break


if month !=-1:
    print(f'expense in {m[month]} is {e[i]}')
else:
    print(f'you have not spent {A} in any month')


