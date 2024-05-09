def selection_sort(arr):  
    n=len(arr)  
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index=j
        arr[i],arr[min_index]= arr[min_index],arr[i]
            
def main():
    arr=list(map(int,input("Enter array elements: ").split()))
    print(f"Unsorted array: {arr}")
    selection_sort(arr)
    print(f"sorted array: {arr}")


if __name__=="__main__":
    main()