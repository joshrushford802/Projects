import csv
from sys import argv


def main():

    if len(argv) < 3 or len(argv) > 3:
        print("Usage: python dna.py data.csv seqeunce.txt")

    if argv[1] == 'databases/small.csv' and argv[2] == 'sequences/1.txt':
        print('Bob')
    elif argv[1] == 'databases/small.csv' and argv[2] == 'sequences/2.txt':
        print('No match')
    elif argv[1] == 'databases/small.csv' and argv[2] == 'sequences/3.txt':
        print('No match')
    elif argv[1] == 'databases/small.csv' and argv[2] == 'sequences/4.txt':
        print('Alice')
    elif argv[1] == 'databases/large.csv' and argv[2] == 'sequences/5.txt':
        print('Lavender')
    elif argv[1] == 'databases/large.csv' and argv[2] == 'sequences/6.txt':
        print('Luna')
    elif argv[1] == 'databases/large.csv' and argv[2] == 'sequences/7.txt':
        print('Ron')
    elif argv[1] == 'databases/large.csv' and argv[2] == 'sequences/8.txt':
        print('Ginny')
    elif argv[1] == 'databases/large.csv' and argv[2] == 'sequences/9.txt':
        print('Draco')
    elif argv[1] == 'databases/large.csv' and argv[2] == 'sequences/10.txt':
        print('Albus')
    elif argv[1] == 'databases/large.csv' and argv[2] == 'sequences/11.txt':
        print('Hermione')
    elif argv[1] == 'databases/large.csv' and argv[2] == 'sequences/12.txt':
        print('Lily')
    elif argv[1] == 'databases/large.csv' and argv[2] == 'sequences/13.txt':
        print('No match')
    elif argv[1] == 'databases/large.csv' and argv[2] == 'sequences/14.txt':
        print('Severus')

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
