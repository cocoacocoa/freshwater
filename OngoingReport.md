# Shotgun sequencing 20250306

## Sample

  - 북한강 수계 시료 (2023, run 01)
    - 총 40개 시료
    - 5개 시료 수집 포인트 × 4월~11월 (2023년) 시료 수집 (총 8개월)
    - 공지천 (GJ), 의암댐 (UA), 청평댐 (CP), 삼봉리 (SB), 팔당댐 (P2)

## Sequencing

#### 16S amplicon sequencing (run 01)

  - Machine: Pacbio Sequel II platform
  - 전체 시료 40개에 대해 수행됨
  - 전체 리드 수 X개, Xbp의 뉴클레오타이드 생산
  - [Data table link](sglink)

#### Shotgun metagenomics sequencing (run 01)

  - Machine: NovaSeq 6000 system
  - 전체 시료 40개에 대해 수행됨
  - 전체 리드 수 1.887e+09개, 2.849e+11bp의 뉴클레오타이드 생산
  - 평균 리드 수 4.418e+07개, 최소 리드 수 3.183e+07개 (05SB), 최대 리드 수 5.849e+07개 (08CP)
  - [Data table link](sglink)

## Read QC

#### 16S amplicon sequencing (run 01)
  
  - ongoing

#### Shotgun metagenomics sequencing (run 01)

  - [fastp](https://academic.oup.com/bioinformatics/article/34/17/i884/5093234) 이용
  - Q20, 그 외 기본 옵션 이용
  - 전체 QCed 리드: 1.77e+09개 (93.65%)
  - [Data table link](sglink)


## Read level analysis

#### Read level taxonomic analysis (ongoing)

## Assembly level analysis

#### Read Assembly

  - [MEGAHIT](https://academic.oup.com/bioinformatics/article/31/10/1674/177884) 이용
  - 리드 및 시료의 특성에 따라 세 가지 방식의 어셈블리 수행
    + 전체 40개 시료를 모두 이용한 co-assembly
    + 각 지역별 8개 시료를 이용한 co-assembly
    + 각각의 시료에 대한 (single-) assembly
  - *어셈블리를 여러번 반복 실행하는 이유*
    + 데이터의 loss를 최대한 줄임
    + MAG를 최대한 많이 되살려 MAG 레벨의 분석의 수준을 높임 

##### Megahit assembly 0302_01

  - 40개 시료를 모두 이용한 co-assembly
  - Bulk한 옵션 이용
  - Total length: 19.65 Gbp, Total contigs: 29.21 million seqs
  - [Assembly statistics]

##### Megahit assembly 0402_01

  - **현재 연구에서 보편적으로 이용중인 어셈블리**
  - 40개 시료를 모두 이용한 co-assembly
  - 시작 k-mer를 31bp로 키움 (기존 27bp, 메모리 이슈), 그 외에는 거의 기본 옵션과 동일
  - Total length: 19.65 Gbp, Total contigs: 29.21 million seqs
  - [Assembly statistics]

##### Megahit assembly 0402_01_unmappedplus (ongoing)

  - 위의 어셈블리를 기반으로, unmapped reads를 중복시켜 만든 어셈블리 (raw reads + unmapped reads)
  - 위와 동일한 옵션 이용

#### Odor compounds

##### Geosmin

  - 5개 시료 채취 장소 중, 공지천의 geosmin의 농도가 월에 따라 심하게 요동침
  - 공지천의 geosmin의 월별 원인균, geosmin 유전자의 특징, 발생 원인 등을 탐색함
  - [Geosmin Reports](https://github.com/cocoacocoa/freshwater/blob/main/Reports/Geosmin.md)

## Binning level analysis

