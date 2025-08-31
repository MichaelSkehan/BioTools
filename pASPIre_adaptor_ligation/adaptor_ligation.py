import adaptors

def ligate(left, seq, right):
    return left + seq + right

if __name__ == '__main__':
    sequence = 'catgggggtttgtaccgtacaccactgagaccgcggtggttgaccagacaaaccacgaaggttctgttaagtaactgaacccaatgtcgttagtgacgcttacctcttaagaggtcactgacctaacaggatcccaccacaattcagcaaattgtgaacatcatcacgttcatctttccctggttgccaatggcccattttcctgtcagtaacgagaaggtcgcgaattcaggcgctttttagactggtcgtagcaacaaaatcaggcacaggcagaacaacaatgatcaaggcgacggacagaaaactgGGTGGAGGCGGTTCTgaaaatttatacttccaatccGGAGGTGGAGGCTCTCGAGCT'
    LEFT = adaptors.LEFT_ADAPTORS['L1']
    RIGHT = adaptors.RIGHT_ADAPTORS['R1']
    print(ligate(LEFT,sequence, RIGHT))