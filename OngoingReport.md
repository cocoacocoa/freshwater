# Shotgun sequencing 20250306

## Sample

  - 북한강 수계 시료 (2023, run 01)
    - 총 40개 시료
    - 5개 시료 수집 포인트 × 4월~11월 (2023년) 시료 수집 (총 8개월)
    - 공지천 (GJ), 의암댐 (UA), 청평댐 (CP), 삼봉리 (SB), 팔당댐 (P2)

## Sequencing

#### 16S amplicon sequencing

  - Machine: Pacbio Sequel II platform
  - 전체 시료 40개에 대해 수행됨
  - 전체 리드 수 X개, Xbp의 뉴클레오타이드 생산
  - [Data table link](sglink)

#### Shotgun metagenomics sequencing

  - Machine: NovaSeq 6000 system
  - 전체 시료 40개에 대해 수행됨
  - 전체 리드 수 1.887e+09개, 2.849e+11bp의 뉴클레오타이드 생산
  - 평균 리드 수 4.418e+07개, 최소 리드 수 3.183e+07개 (05SB), 최대 리드 수 5.849e+07개 (08CP)
  - [Data table link](sglink)

## Read QC

#### 16S amplicon sequencing
  
  - ongoing

#### Shotgun metagenomics sequencing

  - [fastp](https://academic.oup.com/bioinformatics/article/34/17/i884/5093234) 이용
  - Q20, 그 외 기본 옵션 이용
  - 전체 QCed 리드: 1.77e+09개 (93.65%)
  - [Data table link](sglink)


## Assembly

#### Read assembly

  - [MEGAHIT](https://academic.oup.com/bioinformatics/article/31/10/1674/177884) 이용
  - 리드 및 시료의 특성에 따라 세 가지 방식의 어셈블리 수행
    + 전체 40개 시료를 모두 이용한 co-assembly
    + 각 지역별 8개 시료를 이용한 co-assembly
    + 각각의 시료에 대한 (single-) assembly
  - *어셈블리를 여러번 반복 실행하는 이유*
    + 데이터의 loss를 최대한 줄임
    + MAG를 최대한 많이 되살려 MAG 레벨의 분석의 수준을 높임 

##### Total Megahit assembly 0302_01

  - 40개 시료를 모두 이용한 co-assembly
  - 최대한 bulk한 옵션 이용
  - Total length: 19.65 Gbp, Total contigs: 29.21 million seqs
  - [Assembly statistics](https://github.com/cocoacocoa/freshwater/blob/main/Reports/Assembly.md)

##### Total Megahit assembly 0402_01

  - **현재 연구에서 보편적으로 이용중인 어셈블리**
  - 40개 시료를 모두 이용한 co-assembly
  - 시작 k-mer를 31bp로 키움 (기존 27bp, 메모리 이슈), 그 외에는 거의 기본 옵션과 동일
  - Total length: 29.34 Gbp, Total contigs: 43.37 million seqs
  - [Assembly statistics](https://github.com/cocoacocoa/freshwater/blob/main/Reports/Assembly.md)

##### Total Megahit assembly 0404_01 (ongoing)

  - 위의 어셈블리를 기반으로, unmapped reads를 중복시켜 만든 어셈블리 (raw reads + unmapped reads)
  - 위와 동일한 옵션 이용
  - Ongoing

## Binning

#### Strategy

  - [MetaBAT2](https://pmc.ncbi.nlm.nih.gov/articles/PMC6662567/) (+ [VAMB](https://www.nature.com/articles/s41587-020-00777-4), [SemiBin2](https://academic.oup.com/bioinformatics/article/39/Supplement_1/i21/7210480), [GraphMB](https://academic.oup.com/bioinformatics/article/38/19/4481/6668279)) > [DASTools](https://www.nature.com/articles/s41564-018-0171-1) > [CheckM](https://pmc.ncbi.nlm.nih.gov/articles/PMC4484387/) (QC) > [GTDB-tk](https://academic.oup.com/bioinformatics/article/36/6/1925/5626182) (Taxonomic assignment)
  - Preliminary: MetaBAT2 > CheckM (QC) > GTDB-tk
  - High quality: >90% completeness, <5% contamination
  - Middle quality: >50% completeness, <10% contamination

##### (Preliminary) Binning result 01

  - Assembly: Total Megahit assembly 0302_01 이용
  - Binning: MetaBAT2만 이용
  - High quality: 120개, Middle quality: 613개
  - [GTDB-tk result](https://github.com/cocoacocoa/freshwater/blob/main/Reports/120_GTDB_tk.md)

##### (Preliminary) Binning result 02

  - Assembly: Total Megahit assembly 0402_01 이용
  - Binning: MetaBAT2만 이용
  - High quality: 122개, Middle quality: 715개
  - GTDB-tk는 추후 돌려볼 예정

## Odor compounds

#### Geosmin

  - 5개 시료 채취 장소 중, 공지천의 geosmin의 농도가 월에 따라 심하게 요동침
  - 공지천의 geosmin의 월별 원인균, geosmin 유전자의 특징, 발생 원인 등을 탐색함
  - 추가로, geosmin 탐지를 위한 global primer 및 taxa-specific primer에 대한 제작을 시도함
  - [Geosmin Reports](https://github.com/cocoacocoa/freshwater/blob/main/Reports/Geosmin.md)

#### 2-MIB

  - 진행 예정

#### Other compounds

  - 진행 예정

## Virome analysis

#### Viral DNA detection
  

## Resistance & Pathogenicity


## Functional genes & Metabolism


## Environmental correlation



