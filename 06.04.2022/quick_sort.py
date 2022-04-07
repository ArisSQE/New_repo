arr = [5,7,9,2,66,55,22,11]

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr.pop()
    smaller = []
    larger = []
    for i in arr:
        if i < pivot:
            smaller.append(i)
        else:
            larger.append(i)
    return quick_sort(smaller) + [pivot] + quick_sort(larger)

print(quick_sort(arr))