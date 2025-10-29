# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all the numbers stored in the file and calculates their total.

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():
    total_sum = 0
    try:
        with open("numbers.txt") as f:
            lines = f.readlines()
            for line in lines:
                total_sum += int(line)
            print('The sum is', total_sum)
    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("Value error")

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()