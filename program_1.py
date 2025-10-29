# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    ######################
    with open ("names.txt", "r") as f:
        count = 0
        for line in f:
            count += 1
        return count
number_of_names = count_file_lines()
print("There are", number_of_names, "names in names.txt")
# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()