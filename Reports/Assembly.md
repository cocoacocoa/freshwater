# Assembly

##### Total Megahit assembly 0302_01

  - 40개 시료를 모두 이용한 co-assembly
  - 최대한 bulk한 옵션 이용
  - 이용 옵션: --min-count 3 --k-list 31,51,71,91,99
  - Total length: 19.65 Gbp, Total contigs: 29.21 million seqs



##### Total Megahit assembly 0402_01

  - **현재 연구에서 보편적으로 이용중인 어셈블리**
  - 40개 시료를 모두 이용한 co-assembly
  - 시작 k-mer를 31bp로 키움 (기존 27bp, 메모리 이슈), 그 외에는 거의 기본 옵션과 동일
  - 이용 옵션: --min-count 3 --k-list 31,41,51,61,71,81,91,101,111,121,131 --mem-flag 1
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


