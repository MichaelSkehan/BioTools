import csv


def parse_csv(file_path):
    """
    Parse the sequence, left adaptor, and right adaptor from a CSV file.

    :param file_path: The path to the CSV file.
    :type file_path: str
    :return: A list of tuples containing the sequence, left adaptor, and right adaptor.
    :rtype: list
    """
    sequences = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the header row
        for row in reader:
            sequence = row[0]
            left = row[1]
            right = row[2]
            sequences.append((sequence, left, right))
    return sequences

if __name__ == '__main__':
    seq_list = parse_csv('test_csv.csv')
    for seq in seq_list:
        print (seq)