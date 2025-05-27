import algorithms as algo
import files
import time

def test_algorithm(al: str = 'Choose', input: str = 'input.txt', output: str = 'output.out'):
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

    array = files.read(input)
    start_time = 0
    end_time = 0

    if al not in algorithms:
        print(f"Algorithm '{al}' is not recognized.")
    elif al == "Merge":
        start_time = time.time()
        algorithms[al](array, 0, len(array)-1)
        end_time = time.time()
    elif  al ==  "Quick":
        start_time = time.time()
        algorithms[al](array, 0, len(array)-1)
        end_time = time.time()
    else:  
        start_time = time.time()
        algorithms[al](array)
        end_time = time.time()
    
    files.write(array, output)
    
    return algo.SWAP_COUNT, algo.COMPARE_COUNT, (end_time - start_time) 
