def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]


if __name__=="__main__":
    arr=list(map(int,input("Enter array elements: ").split()))
    print(f"Unsorted array: {arr}")
    bubble_sort(arr)
    print(f"sorted array: {arr}")