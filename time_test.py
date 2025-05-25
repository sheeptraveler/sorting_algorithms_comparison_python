import algorithms as algo
import files

algorithms = {

    "Bubble": algo.sort_buble,
    "Insertion": algo.insertion_sort,
    "Quick": algo.quick_Sort,
    "Selection": algo.selection_sort,
    "Merge": algo.merge_sort,
    "Heap": algo.heap_sort,
    "Radix": algo.radix_sort,
    "Count": algo.count_sort,
}

array = files.read()
al = ""

while al not in algorithms:
    print("\n 1.Bubble \n 2.Insertion \n 3.Quick \n 4.Selection \n 5.Merge Sort \n 6.Heapify \n 7.Shell \n 8.Count sort \n")
    al = str((input("Choose algorithm: ")))

if al == "Merge":
    algorithms[al](array, 0, len(array)-1)
elif  al ==  "Quick":
    algorithms[al](array, 0, len(array)-1)
else:  
    algorithms[al](array)

files.write(array)


