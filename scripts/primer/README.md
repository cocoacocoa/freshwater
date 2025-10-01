# Scripts

## Problems and improvements in the current primer search code
  * 

## find_primer_candidates.py

#### Input

  * -f (--fasta): FASTA (aligned FASTA file).
  * -l (--length): Length (primer length, ex. 20).
  * -a (--ambiguous_threshold):
    At each position, nucleotides exceeding this threshold are considered.
    For example, consider a position consisting of 94% G and 6% C.
    If this option is set to 0.1 (10%), C would not exceed this threshold, so this position would be counted as G.
    Conversely, if the threshold is set to 0.05 (5%), both nucleotides would be considered, so this position would be counted as S (G, C) (ex. 0.05).
  * -o (--output_threshold): Output minimum match rate (ex. 0.5).
    
#### Output

```
[4] CATTCYAARGAATGGGCGCG
[revcomp: CGCGCCCATTCYTTRGAATG]
> 34 / 44 Total sequence
> 34 / 44 CYA sequence (77%)

-- Common Primer Location (alignment-level index) --
Start: 1236, End: 1255
...
```
  * [4]: Cases of this primer considering all ambiguous nucleotides.

## find_primer_nogap_v4.py

#### Input

  * -f (--fasta): FASTA (unaligned FASTA file).
  * -p1 (--primer1): Primer 1 sequence (IUPAC supported).
  * -p2 (--primer2): Primer 2 sequence (IUPAC supported).

  * --namelist1: Sequence names that can be matched with primer 1.
  * --namelist2: Sequence names that can be matched with primer 2.
  * --namelist12: Sequence names that can be matched with primer 1 & primer 2 (intersection).
  * --antinamelist1: Sequence names that cannot matched with primer 1.
  * --antinamelist2: Sequence names that cannot be matched with primer 2.
  * --antinamelist12: Sequence names that cannot be matched with primer 1 & primer 2 (union).
  * --namefasta1: Sequences that can be matched with primer 1.
  * --namefasta2: Sequences that can be matched with primer 2.
  * --namefasta12: Sequences that can be matched with primer 1 & primer 2 (intersection).
  * --antinamefasta1: Sequences that cannot matched with primer 1.
  * --antinamefasta2: Sequences that cannot be matched with primer 2.
  * --antinamefasta12: Sequences that cannot be matched with primer 1 & primer 2 (union).


