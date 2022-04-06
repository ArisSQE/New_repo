def selection(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index],arr[i] = arr[i],arr[min_index]
    return arr
a = [5,5,2,3,8,12,4]

print(selection(a))