def sum_list(elements):
    if len(elements)==1:
        return elements[0]
    
    else:
        return elements[0]+sum_list(elements[1:])


print(sum_list([1,2,3,4,5,6]))



