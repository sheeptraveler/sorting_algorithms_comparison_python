#!/bin/bash 

data_sizes=(10000 20000 40000 80000 100000)

for size in "${data_sizes[@]}"; do 
    python3 generateDataSet.py $size

done
