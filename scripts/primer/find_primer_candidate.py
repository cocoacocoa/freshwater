from Bio import AlignIO
from collections import Counter, defaultdict
from itertools import product
import argparse

# IUPAC codes and reverse complements
iupac_codes = {
    frozenset(['A']): 'A', frozenset(['C']): 'C', frozenset(['G']): 'G', frozenset(['T']): 'T',
    frozenset(['A', 'G']): 'R', frozenset(['C', 'T']): 'Y', frozenset(['G', 'C']): 'S', frozenset(['A', 'T']): 'W',
    frozenset(['G', 'T']): 'K', frozenset(['A', 'C']): 'M', frozenset(['C', 'G', 'T']): 'B',
    frozenset(['A', 'G', 'T']): 'D', frozenset(['A', 'C', 'T']): 'H', frozenset(['A', 'C', 'G']): 'V',
    frozenset(['A', 'C', 'G', 'T']): 'N'
}

iupac_weight = {
    'A': 1, 'C': 1, 'G': 1, 'T': 1,
    'R': 2, 'Y': 2, 'S': 2, 'W': 2, 'K': 2, 'M': 2,
    'B': 3, 'D': 3, 'H': 3, 'V': 3,
    'N': 4
}

reverse_complement_map = {
    'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
    'R': 'Y', 'Y': 'R', 'S': 'S', 'W': 'W',
    'K': 'M', 'M': 'K', 'B': 'V', 'D': 'H',
    'H': 'D', 'V': 'B', 'N': 'N'
}

def reverse_complement(seq):
    return ''.join(reverse_complement_map.get(b, 'N') for b in reversed(seq))

def iupac_from_counts(counts, threshold, total):
    freq = {base: count / total for base, count in counts.items() if base != '-'}
    valid_bases = {base for base, f in freq.items() if f >= threshold}
    return iupac_codes.get(frozenset(valid_bases), 'N') if valid_bases else 'N'

def generate_consensus(records, threshold):
    alignment_length = len(records[0].seq)
    consensus = ''
    for i in range(alignment_length):
        col = [record.seq[i] for record in records]
        counts = Counter(col)
        total = sum(counts.values()) - counts.get('-', 0)
        consensus += iupac_from_counts(counts, threshold, total)
    return consensus

def expand_degenerate(primer):
    mapping = {
        'A': 'A', 'C': 'C', 'G': 'G', 'T': 'T',
        'R': 'AG', 'Y': 'CT', 'S': 'GC', 'W': 'AT',
        'K': 'GT', 'M': 'AC',
        'B': 'CGT', 'D': 'AGT', 'H': 'ACT', 'V': 'ACG',
        'N': 'ACGT'
    }
    pools = [mapping[nt] for nt in primer]
    return {''.join(p) for p in product(*pools)}

def analyze_fasta(file, primer_length, ambiguity_threshold, output_threshold):
    alignment = AlignIO.read(file, "fasta")
    records = list(alignment)
    alignment_length = len(records[0].seq)

    consensus = generate_consensus(records, ambiguity_threshold)

    header_groups = defaultdict(list)
    for r in records:
        h = r.id
        group = h[0:3]  # 예: ACT00001 → ACT
        header_groups[group].append((h, str(r.seq).replace("-", "")))

    results = []
    for start in range(0, alignment_length - primer_length + 1):
        window = consensus[start:start + primer_length]
        if '-' in window:
            continue

        weight = 1
        for nt in window:
            weight *= iupac_weight.get(nt, 1)
        if weight > 64:
            continue

        primer_set = expand_degenerate(window)
        matched_headers = []
        group_counts = defaultdict(lambda: [0, 0])  # [match, total]

        for group, seqs in header_groups.items():
            for h, seq in seqs:
                group_counts[group][1] += 1
                for p in primer_set:
                    if p in seq:
                        matched_headers.append(h)
                        group_counts[group][0] += 1
                        break

        if len(matched_headers) / len(records) < output_threshold:
            continue

        result = {
            'start': start,
            'end': start + primer_length - 1,
            'window': window,
            'revcomp': reverse_complement(window),
            'weight': weight,
            'matched': len(matched_headers),
            'total': len(records),
            'groups': {
                g: (m, t, f"{(m/t*100):.0f}%" if t else "0%")
                for g, (m, t) in group_counts.items()
            }
        }
        results.append(result)

    results.sort(key=lambda x: (x['weight'], -x['matched']))
    return results

def print_results(results):
    for r in results:
        print("="*60)
        print(f"[{r['weight']}] {r['window']}")
        print(f"[revcomp: {r['revcomp']}]")
        print(f"> {r['matched']} / {r['total']} Total sequence")
        for g, (m, t, pct) in sorted(r['groups'].items()):
            print(f"> {m} / {t} {g} sequence ({pct})")
        print("\n-- Common Primer Location (alignment level index) --")
        print(f"Start: {r['start']}, End: {r['end']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fasta", required=True, help="aligned FASTA file")
    parser.add_argument("-l", "--length", type=int, default=16, help="primer length")
    parser.add_argument("-a", "--ambiguous_threshold", type=float, default=0.05, help="IUPAC ambiguity threshold (e.g. 0.05)")
    parser.add_argument("-o", "--output_threshold", type=float, default=0.5, help="Output minimum match rate (e.g. 0.5 = 50%)")
    args = parser.parse_args()

    res = analyze_fasta(args.fasta, args.length, args.ambiguous_threshold, args.output_threshold)
    print_results(res)
