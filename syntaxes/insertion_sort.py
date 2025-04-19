A = [-5,2,3,1,-3,-3,4,7,-4]

def insertion_sort(arr):
    n=len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break

insertion_sort(A)
print(A)

#to sort in descending order change the condition in if to (arr[j-1] < arr[j])
