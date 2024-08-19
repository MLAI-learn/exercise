
def merge_sort(arr,key,descending=False):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left,key,descending)
    right = merge_sort(right,key,descending)

    return merge_two_sorted_lists(left, right,key,descending)

def merge_two_sorted_lists(a,b,key,descending=False):
    sorted_list = []

    len_a = len(a)
    len_b = len(b)

    i = j = 0
    if descending:
        while i < len_a and j < len_b:
            c=a[i][key]
            d=b[j][key]
        
        

            if c>d:
                sorted_list.append(a[i])
                i+=1
            else:
                sorted_list.append(b[j])
                j+=1

        while i < len_a:
            sorted_list.append(a[i])
            i+=1
        
        while j < len_b:
           sorted_list.append(b[j])
           j+=1
      
    else:
        
    
        while i < len_a and j < len_b:
            c=a[i][key]
            d=b[j][key]
        
        

            if c<d:
               sorted_list.append(a[i])
               i+=1
            else:
                sorted_list.append(b[j])
                j+=1

        while i < len_a:
            sorted_list.append(a[i])
            i+=1

        while j < len_b:
           sorted_list.append(b[j])
           j+=1
    
    
    
    return sorted_list
    
    
    

if __name__ == '__main__':
   elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
   print(merge_sort(elements, key='name'))