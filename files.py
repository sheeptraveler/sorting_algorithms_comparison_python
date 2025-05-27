import sys


def read(input = "input.txt") -> list[int]:  
    """
    Reads integers from a file named 'input.txt' and returns them as a list.
    If the file does not exist, it returns an empty list.
    """
    try:
        array = []
        with open(input, 'r') as file:
            for line in file:
                for num in line.split(' '):
                    if num.isdigit():
                        array.append(int(num))
            return array
    except FileNotFoundError:
        print(f"File not found. Please ensure {input} exists.")
        return []
    except ValueError:
        print("Invalid data in file. Please ensure all lines contain integers.")
        return []

def write(array, output_file='output.out'):
    """
    Writes the sorted array to a file named 'output.out'.
    If the file cannot be created, it prints an error message.
    """
    try:
        with open(output_file, 'w') as file:
            for item in array:
                file.write(str(item) + ' ')
    except IOError:
        print(f"Error: The file {output_file} could not be created.")
        sys.exit(1)
