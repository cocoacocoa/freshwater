# Shotgun sequencing 20250306

## Sample
- 북한강 수계 시료
  - 총 40개 시료
  - 5개 시료 수집 포인트 × 4월~11월 시료 수집 (총 8개월)
  - 공지천(GJ), 의암댐(UA), 청평댐(CP), 삼봉리(SB), 팔당댐(P2)

## Sequencing

#### 16S amplicon sequencing

##### Pacbio Sequel II platform
  - 모든 시료에 대해 수행됨.
    
    | Sample  | #Reads  | Read Length  | #Total Nucleotide  | Data size  |
    | ------- | ------- | ------------ | ------------------ | ---------- |
    | 04GJ    | 123     | 123          | 123                | 123        |


#### Shotgun metagenomics sequencing

##### NovaSeq 6000 system
  - 모든 시료에 대해 수행됨.
    
    | Sample  | #Reads  | Read Length  | #Total Nucleotide  | Data size  |
    | ------- | ------- | ------------ | ------------------ | ---------- |
    | 04GJ    | 123     | 123          | 123                | 123        |


#### Read QC

##### Pacbio Sequel II platform
  - ongoing

##### NovaSeq 6000 system

  - [fastp](https://academic.oup.com/bioinformatics/article/34/17/i884/5093234) 이용
  - Q20, 그 외 기본 옵션 이용
  - [결과물](ongoing)


## Read level analysis

#### Read level taxonomic analysis (ongoing)

##### Metabuli
  - ongoing


## Assembly level analysis

#### Read Assembly

  - [MEGAHIT](https://academic.oup.com/bioinformatics/article/31/10/1674/177884) 이용
  - 같은 지역 시료끼리 묶은 coassembly


## Binning level analysis

