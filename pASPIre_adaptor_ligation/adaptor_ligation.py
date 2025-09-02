import adaptors

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
    sequence = 'catgggggtttgtaccgtacaccactgagaccgcggtggttgaccagacaaaccacgaaggttctgttaagtaactgaacccaatgtcgttagtgacgcttacctcttaagaggtcactgacctaacaggatcccaccacaattcagcaaattgtgaacatcatcacgttcatctttccctggttgccaatggcccattttcctgtcagtaacgagaaggtcgcgaattcaggcgctttttagactggtcgtagcaacaaaatcaggcacaggcagaacaacaatgatcaaggcgacggacagaaaactgGGTGGAGGCGGTTCTgaaaatttatacttccaatccGGAGGTGGAGGCTCTCGAGCT'
    LEFT = adaptors.LEFT_ADAPTORS['L1']
    RIGHT = adaptors.RIGHT_ADAPTORS['R1']
    print(ligate(LEFT,sequence, RIGHT))