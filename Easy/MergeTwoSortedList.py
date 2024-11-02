def sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) -i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]




def split(array1, array2):
    sort(array1)
    sort(array2)
    array3 = array1 + array2
    sort(array3)

    print(array3)

split(array1, array2)