from Bio.Restriction import *
from Bio.Seq import Seq
from parse_csv import parse_csv
import csv

def extract_target_seq(csv_file, export_csv=False, filename="digest_products.csv"):
    """
    Extract the target sequence from a sequence.
    :param seq: Bio.Seq object.
    :return:
    """
    digest_products = []
    parsed_seq = parse_csv(csv_file)
    rb = NcoI + SacI
    for plasmid in parsed_seq:
        fragment_list = []
        plasmid_seq = Seq(plasmid[0])

        analysis = Analysis(rb, plasmid_seq, linear=False)
        cut_map = analysis.full()

        cut_sites = []

        for re, loc in cut_map.items():
            cut_sites.extend(loc)

        cut_pos = (sorted(set(cut_sites)))

        fragments = []
        for i in range(len(cut_pos) - 1):
            start = cut_pos[i]
            end = cut_pos[(i+1)]

            fragments.append(plasmid_seq[start-1:end-1])

        for frag in fragments:
            if len(frag) == 144:
                fragments.remove(frag)

        if len(fragments) > 1:
            return "Multiple digest products present, check sequence"
        else:
            fragment_list.append(fragments[0])
            fragment_list.append(plasmid[1])
            fragment_list.append(plasmid[2])
        digest_products.append(fragment_list)

    if export_csv:
        with open(filename, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Sequence", "Left_Adaptor", "Right_Adaptor"])  # header
            writer.writerows(digest_products)

    return digest_products


if __name__ == '__main__':

    frag_to_seq = extract_target_seq('test_csv.csv')
    print(frag_to_seq)
    print (len(frag_to_seq))
