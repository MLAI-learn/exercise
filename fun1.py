def calculate_a(a,b,shape='triangle'):
    if shape=='triangle':
        area=1/2*a*b
    elif shape=='rectangle':
        area=a*b
    else:
        area='none'
    return area
    



area_triangle=calculate_a(2,3,'triangle')
print(area_triangle)
area_rectangle=calculate_a(2,3,'rectangle')
print(area_rectangle)
area_=calculate_a(2,3,'h')
print(2,3)


    
