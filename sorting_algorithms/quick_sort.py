def quick_sort(arr,low,high):
    if low < high:
        pivot = partition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot+1,high)

def partition(arr,low,high):
    pivot=arr[low]
    i=low+1
    j=high

    while True:
        while i<=j and arr[i] <=pivot:
            i+=1
        while i<=j and arr[j] >=pivot:
            j-=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
        arr[low],arr[j] = arr[j],arr[low]
        return j

def main():
    arr=list(map(int,input("Enter array elements: ").split()))
    print(f"Unsorted array: {arr}")
    quick_sort(arr,0,len(arr)-1)
    print(f"sorted array: {arr}")


if __name__=="__main__":
    main()
