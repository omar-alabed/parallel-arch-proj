# The parameter direction indicates the sorting direction, ASCENDING or DESCENDING;
# Please note that this only works for arrays of power of 2 size.
def bitonicSort(arr, _direction=True):
    if len(arr) <= 1:

        return arr
    else:
        first = bitonicSort(arr[:len(arr) // 2], True)
        second = bitonicSort(arr[len(arr) // 2:], False)

        return bitonicMerge(_direction, first + second)

def bitonicMerge(direction, arr):
    if len(arr) == 1:
        return arr
    else:
        compAndSwap(direction, arr)
        first = bitonicMerge(direction, arr[:len(arr) // 2])
        second = bitonicMerge(direction, arr[len(arr) // 2:])
        return first + second

def compAndSwap(direction, arr):
    dist = len(arr) // 2
    for i in range(dist):
        if (arr[i] > arr[i + dist]) == direction:
            arr[i], arr[i + dist] = arr[i + dist], arr[i]

