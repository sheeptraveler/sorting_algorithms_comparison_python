import sys
def read():  
    """
    Reads integers from a file named 'input.txt' and returns them as a list.
    If the file does not exist, it returns an empty list.
    """
    if len(sys.argv) != 2:
        print("Usage: python files.py <input_file>")
        sys.exit(1)
    try:
        array = []
        input = sys.argv[1]
        with open(input, 'r') as file:
            for line in file:
                for num in line.split(' '):
                    if num.isdigit():
                        array.append(int(num))
            return array
    except FileNotFoundError:
        print("File not found. Please ensure 'input.txt' exists.")
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
