import sys
import os
import random

if len(sys.argv) != 2:
    print("Usage: python generateDataSet.py <number_of_elements>")
    sys.exit(1)

n = sys.argv[1]
output_dir = "./data/" + str(n) + "/"
if not os.path.exists(output_dir):
    try:
        os.makedirs(output_dir)
    except OSError as e:
        print(f"Error creating directory {output_dir}: {e}")
        sys.exit(1)

array = [i + 1 for i in range(int(n))]
# Ordered Data Set
try:
    dataFileName = output_dir + str(n) + 'orderedSet.in'
    with open(dataFileName, 'w') as dataFile:
        for i in array:
            dataFile.write(str(i) + ' ')
except FileNotFoundError:
    print(f"Error: The file {dataFileName} could not be created.")
    sys.exit(1)

# Inverted Data Set
try:
    dataFileName = output_dir + str(n) + 'invertedOrderedSet.in'
    with open(dataFileName, 'w') as dataFile:
        for i in range(len(array), 0, -1):
            dataFile.write(str(i) + ' ')
except FileNotFoundError:
    print(f"Error: The file {dataFileName} could not be created.")
    sys.exit(1)

# Random Data Set
try:
    random.shuffle(array)
    dataFileName = output_dir + str(n) + 'RandomSet.in'

    with open(dataFileName, 'w') as dataFile:
        for i in array:
            dataFile.write(str(i) + ' ')
except FileNotFoundError:
    print(f"Error: The file {dataFileName} could not be created.")
    sys.exit(1)


