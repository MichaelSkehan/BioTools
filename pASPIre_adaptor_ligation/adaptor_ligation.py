import adaptors
from parse_csv import parse_csv
from restriction_digest import extract_target_seq

def ligate(left, seq, right):
    """
    Ligates a left adaptor, sequence and right adaptor.


    :param left: The left adaptor to ligate.
    :type: str
    :param seq: The sequence to ligate.
    :type: str
    :param right: The right adaptor to ligate.
    :type: str

    :return: The ligated sequence.
    :rtype: str
    """
    return left + seq + right

if __name__ == '__main__':
    list_of_ligated_sequences = []
    for sample in extract_target_seq('test_csv.csv'):
        sequence = sample[0]
        left = adaptors.LEFT_ADAPTORS[sample[1]]
        right = adaptors.RIGHT_ADAPTORS[sample[2]]

        ligated_sequence = ligate(left, sequence, right)
        list_of_ligated_sequences.append(ligated_sequence)

    print(list_of_ligated_sequences)