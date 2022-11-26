
def bubble_sort(array):
    n = len(array)
    print(array)
    print()

    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

a=bubble_sort([5,2,1,3,4,5,3,2,1])

def bin_search(num,array):
    start=0
    stop= len(array) - 1


    while start<=stop:
        mid=(start+stop)//2
        if num== array[mid]:
            return mid
        if array[mid]> num:
            stop=mid-1
        else:
            start=mid+1


