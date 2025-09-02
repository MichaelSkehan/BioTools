import adaptors
from restriction_digest import extract_target_seq
import csv

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

    def main(csv_loc, export_csv=False, filename="ligated_sequences.csv"):
        list_of_ligated_sequences = []
        rows_for_csv = []
        for sample in extract_target_seq(csv_loc):
            sequence = sample[0]
            left = adaptors.LEFT_ADAPTORS[sample[1]]
            right = adaptors.RIGHT_ADAPTORS[sample[2]]

            ligated_sequence = ligate(left, sequence, right)
            list_of_ligated_sequences.append(ligated_sequence)
            rows_for_csv.append([ligated_sequence, sample[1], sample[2]])

        if export_csv:
            with open(filename, mode="w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Sequence", "Left_Adaptor", "Right_Adaptor"])  # header
                writer.writerows(rows_for_csv)
        print (rows_for_csv)


        return list_of_ligated_sequences

    print(main('test_csv.csv', export_csv=True, filename="ligated_sequences.csv"))