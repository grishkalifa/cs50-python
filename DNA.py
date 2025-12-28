import csv
import sys


def main():

    # 1. Check command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py database.csv sequence.txt")
        sys.exit(1)

    database_file = sys.argv[1]
    sequence_file = sys.argv[2]

    # 2. Read DNA sequence into memory
    with open(sequence_file, "r") as file:
        sequence = file.read()

    # 3. Read database CSV into memory
    with open(database_file, "r") as file:
        reader = csv.DictReader(file)
        people = list(reader)

        # Get STR names from header (skip "name")
        strs = reader.fieldnames[1:]

    # 4. Compute longest match for each STR
    str_counts = {}
    for s in strs:
        str_counts[s] = longest_match(sequence, s)

    # 5. Compare against database
    for person in people:
        match = True
        for s in strs:
            if int(person[s]) != str_counts[s]:
                match = False
                break

        if match:
            print(person["name"])
            return

    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    longest_run = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0

        while True:
            start = i + count * sub_len
            end = start + sub_len

            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        longest_run = max(longest_run, count)

    return longest_run


main()
