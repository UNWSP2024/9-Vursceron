# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
#input how many numbers wanted
#open file
#for loop in range 1:inputted number
#in for loop generate random between 1:500
#write to file
import random


def random_numbers():
    with open ("random.txt", "w") as f:
        wanted = int(input("Enter the number of random numbers (do not go over 1000): "))
        if wanted > 1000:
            print("Too many random numbers")
            exit()
        for i in range(wanted):
            number = random.randint(1, 500)
            f.write(str(number) +"\n")

if __name__ == '__main__':
    random_numbers()
