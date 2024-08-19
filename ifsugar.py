l=input('enter sugar level ')
L=int(l)

if L<80:
    print('sugar level is low')
elif L>100:
    print('sugar level is high')
else:
    print('sugar level is normal')