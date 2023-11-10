"""
Code to group and ungroup segmens in comparative wordlists.
"""
from lingpy import Wordlist
from csvw.dsv import UnicodeDictReader
from unicodedata import normalize

def profile_sequence(string, segments, maxlen=None):
    
    max_len = maxlen or max([len(x) for x in segments])
    
    # initialize queue
    queue = [([''], 0, string)]

    out = []
    while queue:
        current_sequence, length, rest = queue.pop(0)
        
        # either add next element or don't
        next_element = rest[0]
        next_string = rest[1:]
        combined_element = current_sequence[-1] + next_element
        clen = len(combined_element)

        if len(rest) > 1:
            if combined_element in segments or not current_sequence[-1] or clen < max_len:
                queue += [[
                    current_sequence[:-1]+[combined_element],
                    length,
                    rest[1:]
                    ]]
            if current_sequence[-1] in segments:
                queue += [[
                    current_sequence + [next_element],
                    length+1,
                    rest[1:]
                    ]]

        else:
            seqA = current_sequence[:-1]+[combined_element]
            seqB = current_sequence + [next_element]
            
            if not [x for x in seqA if (x not in segments and len(x) > 1)]:
                out += [seqA]
            if not [x for x in seqB if (x not in segments and len(x) > 1)]:
                out += [seqB]
    if out:
        return ' '.join(sorted(out, key=lambda x: len([y for y in x if y[0] !=
            '<']))[0])
    return ' '.join(['<{0}>'.format(x) if x in segments else
        x for x in string])
        

def get_profile(filename, delimiter="\t", space="_"):
    profile = {}
    with UnicodeDictReader(filename, delimiter=delimiter) as reader:
        for row in reader:
            profile[row["Grapheme"]] = row
    profile[space] = {k: "NULL" for k in row}
    return profile


def segment(sequence, profile, replace="Grouped", space="_"):
    segments = set(profile)
    segmented = profile_sequence(normalize("NFC", space.join(sequence)), segments).split(" ")
    out = []
    for segment in segmented:
        rep = profile.get(segment, {replace: "«"+segment+"»"})[replace]
        if rep != "NULL":
            out += [rep]
    return out


wl = Wordlist("karen.tsv")
prf = get_profile("karen-profile.tsv")

table = []
for idx, tokens_ in wl.iter_rows("tokens"):
    desegmented, segmented = wl[idx, "desegmented"], " ".join(segment(tokens_,
                                                                      prf))
    if desegmented != segmented:
        print(desegmented, segmented)
        input()
        
    table += [[idx, " ".join(tokens_), " ".join(segment(tokens_, prf))]]

#print(tabulate(table[:20]))
