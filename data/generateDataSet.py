import sys
import random

if len(sys.argv) != 2:
    print("Usage: python generateDataSet.py <number_of_elements>")
    sys.exit(1)

n = sys.argv[1]


array = [i + 1 for i in range(int(n))]
# Ordered Data Set
try:
    dataFileName = str(n) + 'orderedSet.txt'
    with open(dataFileName, 'w') as dataFile:
        for i in array:
            dataFile.write(str(i) + ' ')
except FileNotFoundError:
    print(f"Error: The file {dataFileName} could not be created.")
    sys.exit(1)

# Inverted Data Set
try:
    dataFileName = str(n) + 'invertedOrderedSet.txt'
    with open(dataFileName, 'w') as dataFile:
        for i in range(len(array), 0, -1):
            dataFile.write(str(i) + ' ')
except FileNotFoundError:
    print(f"Error: The file {dataFileName} could not be created.")
    sys.exit(1)

# Random Data Set
try:
    random.shuffle(array)
    dataFileName = str(n) + 'RandomSet.txt'

    with open(dataFileName, 'w') as dataFile:
        for i in array:
            dataFile.write(str(i) + ' ')
except FileNotFoundError:
    print(f"Error: The file {dataFileName} could not be created.")
    sys.exit(1)


