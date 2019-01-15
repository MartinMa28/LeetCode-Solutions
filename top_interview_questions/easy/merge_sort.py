def merge_sort(arr):
    mid = int(len(arr) / 2)
    if mid == 0:
        # the array only has zero or one element, so it's already sorted
        return arr
    else:
        return merge(merge_sort(arr[0:mid]), merge_sort(arr[mid:]))

def merge(arr1, arr2):
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    
    if arr1[0] < arr2[0]:
        return [arr1[0]] + merge(arr1[1:], arr2)
    else:
        return [arr2[0]] + merge(arr1, arr2[1:])


if __name__ == "__main__":
    n1 = [1, 3, 6, 7]
    n2 = [1, 2, 4, 4, 5, 9]
    print(merge(n1, n2))
    test = [-9, -88, 33, 232, 887, 11, 23, 64, -99]
    print(merge_sort(test))