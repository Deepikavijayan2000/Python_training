A = [-5,2,3,1,-3,-3,4,7,-4]
print(A)
def bubble_sort(arr):
    n = len(arr)
    flag= True
    while flag:
        flag = False
        for i in range (1, n):
            if arr[i-1] > arr[i]:
                flag = True
                arr[i-1], arr[i] = arr[i], arr[i-1]

bubble_sort(A)
print(A)

#if you want to sort the array in descending order 
#then change the condition in if to (arr[i-1]<arr[i])
