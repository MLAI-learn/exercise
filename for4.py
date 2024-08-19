for i in range(5):
    print(f'you ran {i+1} km, want to take break')
    tired=input('r u tired?')
    if tired=='yes':
        break

    
if i==4:
    print(f'you completed the race, u ran {i+1}km')
else:
    print(f'race incomplete,you ran {i+1}km')



