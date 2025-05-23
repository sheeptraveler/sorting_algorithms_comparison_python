import algorithms as algo

algorithms = {

    "Bubble": algo.sort_buble,
    "Insertion": algo.insertion_sort,
    "Quick": algo.quick_Sort,
    "Selection": algo.selection_sort,
    "Merge": algo.merge_sort,
    "Heap": algo.heap_sort,
    "Shell": algo.shell_sort,
    "Count": algo.count_sort,
}

print("\n 1.Bubble \n 2.Insertion \n 3.Quick \n 4.Selection \n 5.Merge Sort \n 6.Heapify \n 7.Shell \n 8.Count sort \n")
al = str((input("Choose algorithm: ")))

array = [3,2, 1]
print(array)
array = algorithms[al](array)
print(array)



