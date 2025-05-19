# Shotgun sequencing 20250306

## Sample

- 북한강 수계 시료
  - 총 40개 시료
  - 5개 시료 수집 포인트 × 4월~11월 시료 수집 (총 8개월)
  - 공지천(GJ), 의암댐(UA), 청평댐(CP), 삼봉리(SB), 팔당댐(P2)

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
  - [Data table link](sglink)

## Read QC

#### 16S amplicon sequencing (run 01)
  
  - ongoing

#### Shotgun metagenomics sequencing (run 01)

  - [fastp](https://academic.oup.com/bioinformatics/article/34/17/i884/5093234) 이용
  - Q20, 그 외 기본 옵션 이용
  - [Data table link](sglink)


## Read level analysis

#### Read level taxonomic analysis (ongoing)



## Assembly level analysis

#### Read Assembly

  - [MEGAHIT](https://academic.oup.com/bioinformatics/article/31/10/1674/177884) 이용
  - [MEGAHIT 옵션 탐색](mgoptlink)
  - 같은 지역 시료끼리 묶은 coassembly 생산


## Binning level analysis

