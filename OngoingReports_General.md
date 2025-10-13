# Shotgun sequencing 20250306

- Root directory: @panpyro, /panpyro/bravo/bhpark/kwjang_2025/metagenome/20250306_shotgun

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
  - 파일 위치: [root directory]/Lane_1/
  - [Data table link](sglink)

## Read QC

#### 16S amplicon sequencing
  
  - ongoing

#### Shotgun metagenomics sequencing

  - [fastp](https://academic.oup.com/bioinformatics/article/34/17/i884/5093234) 이용
  - Q20, 그 외 기본 옵션 이용
  - 전체 QCed 리드: 1.77e+09개 (93.65%)
  - 파일 위치: [root directory]/Lane_1/
  - [Data table link](sglink)


## Assembly

#### Read assembly

  - [MEGAHIT](https://academic.oup.com/bioinformatics/article/31/10/1674/177884) 이용
  - 리드 및 시료의 특성에 따라 두 가지 방식의 어셈블리 수행
    + 전체 40개 시료를 모두 이용한 co-assembly
    + 각각의 시료에 대한 (single-) assembly

##### Total Megahit assembly 0302_01

  - 40개 시료를 모두 이용한 co-assembly
  - 최대한 bulk한 옵션 이용
  - 파일 위치: [root directory]/coassembly/total/total_assembly_megahit_0302_01
  - Total length: 19.65 Gbp, Total contigs: 29.21 million seqs
  - [Assembly statistics](https://github.com/cocoacocoa/freshwater/blob/main/Reports/Assembly.md)

##### Total Megahit assembly 0402_01

  - **현재 연구에서 보편적으로 이용중인 어셈블리**
  - 40개 시료를 모두 이용한 co-assembly
  - 시작 k-mer를 31bp로 키움 (기존 27bp, 메모리 이슈), 그 외에는 거의 기본 옵션과 동일
  - 파일 위치: [root directory]/coassembly/total/total_assembly_megahit_0402_01
  - Total length: 29.34 Gbp, Total contigs: 43.37 million seqs
  - [Assembly statistics](https://github.com/cocoacocoa/freshwater/blob/main/Reports/Assembly.md)

##### Total Megahit assembly 0403_01

  - 40개 시료를 모두 이용한 co-assembly
  - 위의 어셈블리를 기반으로, unmapped reads를 중복시켜 만든 어셈블리 (raw reads + unmapped reads)
  - 위와 동일한 옵션 이용
  - 파일 위치: @panpyro, /panpyro/charlie/bhpark/kwjang_2025/metagenome/20250306_shotgun/coassembly/total/reads/total_assembly_megahit_0403_01 (현재 삭제됨)
  - 그 결과, total length, total contig의 평가 결과가 0402_01과 비슷하거나 좋지 못함
  - **최종 폐기**

##### Single Megahit assembly 01

  - 각각의 시료를 이용한 개별 assembly, 40개 시료 모두 개별로 수행
  - meta-sensitive 옵션 이용, 될 수 있는한 sensitive하게 어셈블리 획득 시도
  - 파일 위치: [root directory]/assembly/megahit
  - Total length: X.XX Gbp, Total contigs: 1.60 million seqs ~ 3.14 million seqs (average 2.34 million seqs)
  - [Assembly statistics](https://github.com/cocoacocoa/freshwater/blob/main/Reports/Assembly.md)
    
## Binning

#### Strategy

  - [MetaBAT2](https://pmc.ncbi.nlm.nih.gov/articles/PMC6662567/) (+ [COMEBin](https://www.nature.com/articles/s41467-023-44290-z) > [DASTools](https://www.nature.com/articles/s41564-018-0171-1)) > [CheckM](https://pmc.ncbi.nlm.nih.gov/articles/PMC4484387/) (QC) > [GTDB-tk](https://academic.oup.com/bioinformatics/article/36/6/1925/5626182) (Taxonomic assignment)
  - Preliminary: MetaBAT2 > CheckM (QC) > GTDB-tk
  - Preliminary (COMEBin): COMEBin > CheckM (QC) > GTDB-tk
  - 분류 기준 (CheckM 결과 기준)
    - Near-complete: completeness ≥ 90% & contamination ≤ 5%
    - High-quality: completeness ≥ 70% & contamination ≤ 10%
    - Medium-quality: completeness ≥ 50% & contamination ≤ 10%

##### (Preliminary) Binning result 01

  - Assembly: Total Megahit assembly 0302_01 이용
  - Binning: MetaBAT2만 이용
  - 파일 위치: [root directory]/coassembly/total/binning/total_assembly_megahit_0302_01/metabat2/
  - ~~High quality: 120개, Middle quality: 613개~~
  - [GTDB-tk result](https://github.com/cocoacocoa/freshwater/blob/main/Reports/120_GTDB_tk.md)

##### (Preliminary) Binning result 02

  - Assembly: Total Megahit assembly 0402_01 이용
  - Binning: MetaBAT2만 이용
  - 파일 위치: [root directory]/coassembly/total/binning/total_assembly_megahit_0402_01/metabat2/
  - **Near-complete: 122개, High-quality: 480개, Midium-quality: 716개**
  - GTDB-tk 돌렸음, 파일 업로드 예정

##### (Preliminary) Binning result 03 (COMEBin)

  - Assembly: Total Megahit assembly 0402_01 이용
  - Binning: **COMEBin만 이용**
  - 파일 위치: [root directory]/coassembly/total/binning/total_assembly_megahit_0402_01/comebin/
  - **Near-complete: 77개, High-quality: 289개, Midium-quality: 374개**
  - GTDB-tk 돌릴 예정, 파일 업로드 예정
  - 앞의 Binning result 02와 합쳐서, DASTool 돌려볼 예정

##### (Preliminary) Single Binning result 01

  - Assembly: Single Megahit assembly 01 이용
  - Binning: MetaBAT2만 이용
  - 파일 위치: [root directory]/assembly/binning/
  - **Near-complete: 192개, High-quality: 591개, Midium-quality: 889개**
  - GTDB-tk 돌렸음, 파일 업로드 예정

## Protein Annotation

#### Strategy

  - 단백질 예측 후 여러 프로그램을 이용하여 주석달기 진행
  - 단백질의 빈도는 두 가지로 측정
    - 단백질이 위치한 assembly의 빈도 (mapping된 read의 빈도)
    - 단백질이 위치한 assembly를 포함하고 있는 bin의 빈도 (binning이 된 assembly일 경우)

##### Annotation result for Megahit assembly 0402_01
  
  - Protein prediction: [Prodigal](https://github.com/hyattpd/Prodigal) on whole assembly
  - Protein assignment
    - [EggNOG-mapper](https://github.com/eggnogdb/eggnog-mapper?tab=readme-ov-file): 기본 옵션 이용, v2.1.13 (eggNOG 5.0)
  - 탄소 순환, 질소 순환 등과 관련된 주요 유전자(probe genes) 탐색 목적
  - 파일 위치: [root directory]/protein/total_assembly_megahit_0402_01/eggnog/
