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
  - Total length: 19.65 Gbp, Total contigs: 29.21 million seqs

