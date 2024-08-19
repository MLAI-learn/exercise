#lumuto partition

def swap(arr,a,b,):
    arr[a],arr[b]=arr[b],arr[a]

def partition(arr,s,e):
    pivot=arr[e]

    i=s
    for j in range(s,e):
        if arr[j]<=pivot:
            swap(arr,i,j)
            i+=1
    swap(arr,i,e)
    return i

def quick_sort(arr,s,e):
    if s>=e or s<0:
        return
    
    p=partition(arr,s,e)
    quick_sort(arr,s,p-1)
    quick_sort(arr,p+1,e)


if __name__=='__main__':
     elements = [11,9,29,7,2,15,28]
     quick_sort(elements, 0, len(elements)-1)
     print(elements)

tests = [
        [11,9,29,7,2,15,28],
        [3,11, 7,7, 9,7, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')