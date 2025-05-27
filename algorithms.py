#from memory_profiler import profile

SWAP_COUNT = 0
COMPARE_COUNT = 0

def swap(A, i, j):
    a = A[j]
    A[j] = A[i]
    A[i] = a

# O(n²) #########################################################################################
#@profile
def sort_buble(arr):
    global SWAP_COUNT, COMPARE_COUNT
    if (len(arr) == 1):
        return
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            COMPARE_COUNT += 1  
            if (arr[j] > arr[j + 1]):
                SWAP_COUNT += 1
                swap(arr, j, j + 1)
    # return arr

def insertion_sort(arr):
    global SWAP_COUNT, COMPARE_COUNT
    if(len(arr)==1):
        return
    for i in range(1,len(arr)):
        j = i
        COMPARE_COUNT += 1
        while(j>0 and arr[j-1]>arr[j]):
            SWAP_COUNT += 1
            swap(arr,j,j-1)
            j-=1
    # return arr

def selection_sort(arr):
    global SWAP_COUNT, COMPARE_COUNT
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            COMPARE_COUNT += 1
            if(arr[j]<arr[min]):
                min=j
          #  yield arr
        if(min!=i):
            SWAP_COUNT += 1
            swap(arr,i,min)
    # return arr

# O(n logn) #####################################################################################
def merge_sort(arr,lb,ub):
    if(ub<=lb):
        return
    elif(lb<ub):
        mid =(lb+ub)//2
        merge_sort(arr,lb,mid)
        merge_sort(arr,mid+1,ub)
        merge(arr,lb,mid,ub)

def merge(arr,lb,mid,ub):
    global SWAP_COUNT, COMPARE_COUNT
    new = []
    i = lb
    j = mid+1
    while(i<=mid and j<=ub):
        COMPARE_COUNT += 1
        if(arr[i]<arr[j]):
            new.append(arr[i])
            i+=1
        else:
            new.append(arr[j])
            j+=1
    if(i>mid):
        while(j<=ub):
            new.append(arr[j])
            j+=1
    else:
        while(i<=mid):
            new.append(arr[i])
            i+=1
    for i,val in enumerate(new):
        arr[lb+i] = val

# NOT WORKING ##########################################################################
def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            swap(array, i, j)
            #(array[i], array[j]) = (array[j], array[i])
    swap(array, i+1, high)
    #(array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quick_Sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_Sort(array, low, pi - 1)
        quick_Sort(array, pi + 1, high)

def heap_sort(arr):
    global SWAP_COUNT, COMPARE_COUNT
    n = len(arr)
    for i in range(n,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        SWAP_COUNT += 1
        swap(arr,0,i)
        heapify(arr,i,0)

def heapify(arr,n,i):
    global SWAP_COUNT, COMPARE_COUNT
    largest = i
    l = i*2+1
    r = i*2+2
    while(l<n and arr[l]>arr[largest]):
        COMPARE_COUNT += 1
        largest = l
    while(r<n and arr[r]>arr[largest]):
        COMPARE_COUNT += 1
        largest = r
    if(largest!=i):
        SWAP_COUNT += 1
        swap(arr,i,largest)
        heapify(arr,n,largest)

# O(n+k) ou O(nk) ###############################################################################
def count_sort(arr):
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m

    for a in arr:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1

# Radix Sort
def countingSort(arr, exp1): 
  
    n = len(arr) 
  
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
  
    # initialize count array as 0 
    count = [0] * (10) 
  
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[int((index)%10)] += 1
  
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    # Build the output array 
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = arr[i] 
        count[int((index)%10)] -= 1
        i -= 1
  
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 

# Method to do Radix Sort
def radix_sort(arr):

    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 // exp > 0:
        countingSort(arr,exp)
        exp *= 10





