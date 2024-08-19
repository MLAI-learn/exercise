#optmized version of remove duplicates
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def remove_duplicates(arr):
    return list(dict.fromkeys(arr))

if __name__ == '__main__':
    elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]

    print(f'Given unsorted list: {elements}')
    shell_sort(elements)
    print(f'List after Sorting : {elements}')
    elements = remove_duplicates(elements)
    print(f'List after Removing Duplicates: {elements}')
