# Assembly

##### GJ Megahit assembly 03

  - 공지천 8개 시료를 이용한 co-assembly
  - 리드를 시료별로 따로 넣지 않고, 뭉쳐서 두 파일로 넣음 (R1, R2), 기본 옵션 중 --presets meta-large 이용
  - 이용 옵션: --presets meta-large (--k-min 27 --k-max 127 --k-step 10)
  - 파일 위치: [root directory]/coassembly/GJtotal/GJtotal_assembly_megahit_03/final.contigs.fa
  - Total length: 10.23 Gbp, Total contigs: 18.15 million seqs
    - Longest Contig: 267,309
    - Shortest Contig: 200
    - Total Length: 10,231,351,952
    - Total Contigs: 18,150,821
    - 100 bp Length Sum: 10,231,351,952 (100.00%)
    - 100 bp Contig Count: 18,150,821 (100.00%)
    - 500 bp Length Sum: 5,956,335,414 (58.22%)
    - 500 bp Contig Count: 6,169,529 (33.99%)
    - 1000 bp Length Sum: 2,822,130,842 (27.58%)
    - 1000 bp Contig Count: 1,471,659 (8.11%)
    - 5000 bp Length Sum: 491,013,318 (4.80%)
    - 5000 bp Contig Count: 52,260 (0.29%)
    - 10000 bp Length Sum: 227,102,158 (2.22%)
    - 10000 bp Contig Count: 12,580 (0.07%)
    - A Count: 2,578,779,581
    - A Ratio: 25.20%
    - T Count: 2,503,254,489
    - T Ratio: 24.47%
    - G Count: 2,565,901,382
    - G Ratio: 25.08%
    - C Count: 2,583,416,500
    - C Ratio: 25.25%
    - N Count: 0
    - N Ratio: 0.00%
    - N20: 1,343
    - N50: 579
    - N80: 362
    - L20: 794,293
    - L50: 4,604,369
    - L80: 11,481,687


##### GJ Megahit assembly 0302

  - 공지천 8개 시료를 이용한 co-assembly
  - 기본 옵션 중 --presets meta-large 이용
  - 이용 옵션: --presets meta-large (--k-min 27 --k-max 127 --k-step 10)
  - 파일 위치: [root directory]/coassembly/GJtotal/GJtotal_assembly_megahit_0302/final.contigs.fa
  - Total length: XX.XX Gbp, Total contigs: XX.XX million seqs


##### Total Megahit assembly 0302_01

  - 40개 시료를 모두 이용한 co-assembly
  - 최대한 bulk한 옵션 이용
  - 이용 옵션: --min-count 3 --k-list 31,51,71,91,99
  - 파일 위치: [root directory]/coassembly/total/total_assembly_megahit_0302_01/final.contigs.fa
  - Total length: 19.65 Gbp, Total contigs: 29.21 million seqs
    - Longest Contig: 445,459
    - Shortest Contig: 200
    - Total Length: 19,653,312,470
    - Total Contigs: 29,208,744
    - 100 bp Length Sum: 19,653,312,470 (100.00%)
    - 100 bp Contig Count: 29,208,744 (100.00%)
    - 500 bp Length Sum: 13,822,012,862 (70.33%)
    - 500 bp Contig Count: 11,217,868 (38.41%)
    - 1000 bp Length Sum: 8,773,223,366 (44.64%)
    - 1000 bp Contig Count: 3,822,111 (13.09%)
    - 5000 bp Length Sum: 2,401,617,042 (12.22%)
    - 5000 bp Contig Count: 238,760 (0.82%)
    - 10000 bp Length Sum: 1,244,225,645 (6.33%)
    - 10000 bp Contig Count: 66,499 (0.23%)
    - A Count: 5,007,601,437
    - A Ratio: 25.48%
    - T Count: 4,873,771,180
    - T Ratio: 24.80%
    - G Count: 4,868,676,027
    - G Ratio: 24.77%
    - C Count: 4,903,263,826
    - C Ratio: 24.95%
    - N Count: 0
    - N Ratio: 0.00%
    - N20: 2,844
    - N50: 848
    - N80: 391
    - L20: 657,687
    - L50: 4,968,798
    - L80: 15,531,262


##### Total Megahit assembly 0402_01

  - **현재 연구에서 보편적으로 이용중인 어셈블리**
  - 40개 시료를 모두 이용한 co-assembly
  - 시작 k-mer를 31bp로 키움 (기존 27bp, 메모리 이슈), min-count를 3으로 설정, 그 외에는 거의 기본 옵션과 동일
  - 이용 옵션: --min-count 3 --k-list 31,41,51,61,71,81,91,101,111,121,131 --mem-flag 1
  - 파일 위치: [root directory]/coassembly/total/total_assembly_megahit_0402_01/final.contigs.fa
  - Total length: 29.34 Gbp, Total contigs: 43.37 million seqs
    - Longest Contig: 582,015
    - Shortest Contig: 200
    - Total Length: 29,339,179,497
    - Total Contigs: 43,368,720
    - 100 bp Length Sum: 29,339,179,497 (100.00%)
    - 100 bp Contig Count: 43,368,720 (100.00%)
    - 500 bp Length Sum: 20,710,414,191 (70.59%)
    - 500 bp Contig Count: 17,817,330 (41.08%)
    - 1000 bp Length Sum: 12,346,290,335 (42.08%)
    - 1000 bp Contig Count: 5,422,366 (12.50%)
    - 5000 bp Length Sum: 3,347,263,313 (11.41%)
    - 5000 bp Contig Count: 332,703 (0.77%)
    - 10000 bp Length Sum: 1,727,810,659 (5.89%)
    - 10000 bp Contig Count: 91,431 (0.21%)
    - A Count: 7,450,314,033
    - A Ratio: 25.39%
    - T Count: 7,238,502,328
    - T Ratio: 24.67%
    - G Count: 7,299,887,242
    - G Ratio: 24.88%
    - C Count: 7,350,475,894
    - C Ratio: 25.05%
    - N Count: 0
    - N Ratio: 0.00%
    - N20: 2,621
    - N50: 792
    - N80: 406
    - L20: 1,058,791
    - L50: 8,049,747
    - L80: 23,956,304


