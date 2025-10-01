import argparse
import re
from collections import defaultdict
import statistics

IUPAC = {
    'A': 'A', 'C': 'C', 'G': 'G', 'T': 'T', 'U': 'U',
    'W': '[AT]', 'S': '[CG]', 'M': '[AC]', 'K': '[GT]',
    'R': '[AG]', 'Y': '[CT]', 'B': '[CGT]', 'D': '[AGT]',
    'H': '[ACT]', 'V': '[ACG]', 'N': '[ACGT]'
}

def iupac_to_regex(seq):
    return ''.join(IUPAC.get(base.upper(), base) for base in seq)

def parse_fasta(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    records = {}
    for i in range(0, len(lines), 2):
        header = lines[i].strip()
        seq = lines[i+1].strip()
        records[header] = seq
    return records

def find_single_primer_matches(records, primer_regex):
    matched = {}
    unmatched = set()
    starts = []
    ends = []
    stats = defaultdict(int)

    for header, seq in records.items():
        matches = list(re.finditer(primer_regex, seq))
        prefix = header[1:4]
        if len(matches) == 1:
            m = matches[0]
            start = m.start()
            end = m.end() - 1
            matched[header] = (start, end)
            starts.append(start)
            ends.append(end)
            stats[prefix] += 1
        elif len(matches) > 1:
            raise ValueError(f"[ERROR] The primer was found more than once in the {header}.")
        else:
            unmatched.add(header)

    return matched, unmatched, stats, starts, ends

def summarize_positions(positions):
    if not positions:
        return "N/A"
    return f"{min(positions)} - {max(positions)} (average {statistics.mean(positions):.1f})"

def summarize_prefixes(matched, total_records):
    all_prefixes = sorted({h[1:4] for h in total_records})
    counts = defaultdict(int)
    for h in matched:
        counts[h[1:4]] += 1

    for prefix in all_prefixes:
        total = sum(1 for h in total_records if h[1:4] == prefix)
        match = counts.get(prefix, 0)
        percent = (match / total * 100) if total > 0 else 0
        print(f"> {match} / {total} {prefix} sequence ({percent:.0f}%)")

def write_name_list(headers, output_file):
    with open(output_file, 'w') as f:
        for h in sorted(headers):
            f.write(f"{h}\n")

def write_fasta(headers, records, output_file):
    with open(output_file, 'w') as f:
        for h in sorted(headers):
            f.write(f"{h}\n{records[h]}\n")

def main():
    parser = argparse.ArgumentParser(description="Primer pair matcher with output options (v4)")
    parser.add_argument("-f", "--fasta", required=True, help="Input unaligned FASTA file")
    parser.add_argument("-p1", "--primer1", required=True, help="Primer 1 sequence (IUPAC supported)")
    parser.add_argument("-p2", "--primer2", required=True, help="Primer 2 sequence (IUPAC supported)")

    parser.add_argument("--namelist1")
    parser.add_argument("--namelist2")
    parser.add_argument("--namelist12")
    parser.add_argument("--antinamelist1")
    parser.add_argument("--antinamelist2")
    parser.add_argument("--antinamelist12")
    parser.add_argument("--namefasta1")
    parser.add_argument("--namefasta2")
    parser.add_argument("--namefasta12")
    parser.add_argument("--antinamefasta1")
    parser.add_argument("--antinamefasta2")
    parser.add_argument("--antinamefasta12")

    args = parser.parse_args()

    records = parse_fasta(args.fasta)
    total = len(records)

    regex1 = iupac_to_regex(args.primer1)
    regex2 = iupac_to_regex(args.primer2)

    matched1, unmatched1, stats1, starts1, ends1 = find_single_primer_matches(records, regex1)
    matched2, unmatched2, stats2, starts2, ends2 = find_single_primer_matches(records, regex2)

    common_headers = set(matched1) & set(matched2)
    common_unmatched = set(records) - common_headers
    amplicon_lengths = []
    for h in common_headers:
        s1, e1 = matched1[h]
        s2, e2 = matched2[h]
        amp_len = abs(s2 - e1) + 1 if s2 >= e1 else abs(e2 - s1) + 1
        amplicon_lengths.append(amp_len)

    print(f"[Primer1] {len(matched1)} / {total} matched")
    summarize_prefixes(matched1, records)
    print(f"Start: {summarize_positions(starts1)}")
    print(f"End:   {summarize_positions(ends1)}")

    print(f"\n[Primer2] {len(matched2)} / {total} matched")
    summarize_prefixes(matched2, records)
    print(f"Start: {summarize_positions(starts2)}")
    print(f"End:   {summarize_positions(ends2)}")

    print(f"\n[Intersection] {len(common_headers)} / {total} matched both primers")
    summarize_prefixes(common_headers, records)
    if amplicon_lengths:
        print(f"Amplicon length: {min(amplicon_lengths)} - {max(amplicon_lengths)} (average {statistics.mean(amplicon_lengths):.1f} bp)")
    else:
        print("Amplicon length: N/A")

    # Export options
    if args.namelist1: write_name_list(matched1, args.namelist1)
    if args.namelist2: write_name_list(matched2, args.namelist2)
    if args.namelist12: write_name_list(common_headers, args.namelist12)

    if args.antinamelist1: write_name_list(unmatched1, args.antinamelist1)
    if args.antinamelist2: write_name_list(unmatched2, args.antinamelist2)
    if args.antinamelist12: write_name_list(common_unmatched, args.antinamelist12)

    if args.namefasta1: write_fasta(matched1, records, args.namefasta1)
    if args.namefasta2: write_fasta(matched2, records, args.namefasta2)
    if args.namefasta12: write_fasta(common_headers, records, args.namefasta12)

    if args.antinamefasta1: write_fasta(unmatched1, records, args.antinamefasta1)
    if args.antinamefasta2: write_fasta(unmatched2, records, args.antinamefasta2)
    if args.antinamefasta12: write_fasta(common_unmatched, records, args.antinamefasta12)

if __name__ == "__main__":
    main()
