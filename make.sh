#!/bin/bash 

data_sizes=(10000 20000 40000 80000 100000)
  for size in "${data_sizes[@]}"; do 
    python3 generateDataSet.py $size
  done
    
algorithms=("Bubble" "Insertion" "Selection" "Merge" "Quick" "Heap" "Counting" "Radix")

orders=("orderedSet" "invertedOrderedSet" "RandomSet")

  for algo in "${algorithms[@]}"; do 
    for size in "${data_sizes[@]}"; do 
      for order in "${orders[@]}"; do
        python3 main.py $algo $size $order
      done
    done
  done
