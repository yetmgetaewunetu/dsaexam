def mergeSort(array):
    if len(array) > 1:
        mid = len(array) //2
        left = array[:mid]
        right = array[mid:]
        mergeSort(left)
        mergeSort(right)
        merge(array, left ,right)

def merge(array, left, right):
    i  = j = k = 0
    while i < len(left) and  j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k]= right[j]
            j+= 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i+=1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


nums = [6,1,9,3,0,2,6,8,0,3,6,8,1,6,9,2,3]
mergeSort(nums)
print(nums)
