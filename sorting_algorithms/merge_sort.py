def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid= len(arr)//2
    l_half=arr[:mid]
    r_half=arr[mid:]
    l_half=merge_sort(l_half)
    r_half=merge_sort(r_half)
    return merge(l_half,r_half)

def merge(left,right):
    new=[]
    i,j=0,0

    while i< len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1

    new.extend(left[i:])
    new.extend(right[j:])
    return new


def main():
    arr=list(map(int,input("Enter array elements: ").split()))
    print(f"Unsorted array: {arr}")
    sorted_array=merge_sort(arr)
    print(f"sorted array: {sorted_array}")


if __name__=="__main__":
    main()