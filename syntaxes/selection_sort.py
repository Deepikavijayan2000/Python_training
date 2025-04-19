A = [-5,2,3,1,-3,-3,4,7,-4]

def selection_sort(arr):
    n = len(arr)
    for i in range (1, n):
        min_index = i
        for j in range (i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j 
        arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sort(A)
print(A)