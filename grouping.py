"""
Code to group and ungroup segmens in comparative wordlists.
"""
from lingpy import Wordlist
from linse.transform import SegmentGrouper
from tabulate import tabulate

sg = SegmentGrouper.from_file("karen-profile.tsv", normalization="NFC", grapheme_column="Grapheme")

wl = Wordlist("karen.tsv")

table = []
for idx, tokens_ in wl.iter_rows("tokens"):
    desegmented, segmented = wl[idx, "desegmented"], " ".join(sg(" ".join(tokens_),
                                                                 column="Grouped"))
    if desegmented != segmented:
        print(desegmented, segmented)
        input()
        
    table += [[idx, " ".join(tokens_), " ".join(sg(" ".join(tokens_), column="Grouped"))]]

print(tabulate(table))
