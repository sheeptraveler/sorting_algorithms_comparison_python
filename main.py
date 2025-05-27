import test_algorithm
import os
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
            print("Usage: python main.py <algorithm_name> <data_size> <data_order>")
            sys.exit(1)

    al = sys.argv[1]
    data_size = sys.argv[2]
    data_order = sys.argv[3]
    
    orders = ["orderedSet", "invertedOrderedSet", "RandomSet"]

    if data_order not in orders:
        print(f"Invalid data order. Choose from {orders}.")
        sys.exit(1)
    
    
    input = f"./data/{data_size}/in/{data_size}{data_order}.in"
    output = f"./data/{data_size}/out/{data_size}{data_order}.out"

    OUTPUT_DIR = f"./data/{data_size}/out/"

    if not os.path.exists(OUTPUT_DIR):
        try:
            os.makedirs(OUTPUT_DIR)
        except OSError as e:
            print(f"Error creating directory {OUTPUT_DIR}: {e}")
            sys.exit(1)



    swap_conut = 0
    compare_count = 0
    
    swap_count, compare_count, elapsed_time = test_algorithm.test_algorithm(al, input, output)  # Call the function to run the tests
    
    try:
        with open('metrics', 'a') as metrics:
            metrics.write(f"{al} {data_size} {data_order} Swaps {swap_count} Comparison {compare_count} Time {elapsed_time}\n") 
    except FileNotFoundError:
        print(f"Error: The file metrics could not be created.")
        sys.exit(1)
