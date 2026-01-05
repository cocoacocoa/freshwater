README

## 📊 bin_table_combo.tsv 데이터 가이드

이 테이블은 **MetaBAT2**를 통해 생성된 각 Bin을 행(Row)으로 하며, 각 샘플별 풍부도(Abundance)와 품질 및 분류 정보를 통합한 데이터 시트입니다.

---

### 1. 데이터 개요 및 생성 과정
* **Bin 생성**: MetaBAT2를 사용하여 Co-assembly 결과물로부터 Bin을 추출하였습니다. (상세 내용은 `binning` 디렉토리 참조)
* **Abundance 산출**:
    1.  Co-assembly로 만들어진 Bin에 각 월별 Raw Read 데이터를 매핑하여 1차 매핑 파일을 생성합니다.
    2.  각 Contig에 매핑된 리드 수를 해당 Bin 단위로 합산(Sum)하여 최종 **abs** 값을 산출합니다.

---

### 2. 주요 열(Column) 상세 설명

#### A. 풍부도 데이터 (Abundance Metrics)
각 샘플명 뒤에 붙는 접미사에 따라 아래와 같은 의미를 갖습니다. (예: `04CP_abs`, `04CP_rel1` 등)

| 항목 | 설명 | 비고 |
| :--- | :--- | :--- |
| **abs** | 해당 샘플에서 특정 Bin에 매핑된 Raw Read 수의 총합 | **0**일 경우 해당 시료에서 발견되지 않음을 의미 |
| **rel1** | 해당 시료의 **전체 리드 수**(Unmapped 포함) 대비 상대 빈도 | $rel1 = \frac{\text{Bin mapped reads}}{\text{Total reads in sample}}$ |
| **rel2** | 해당 시료의 **매핑된 리드 수** 대비 상대 빈도 | $rel2 = \frac{\text{Bin mapped reads}}{\text{Total mapped reads}}$ |
| **rel3** | 해당 시료의 매핑된 리드 중 **Binning이 된 리드 수** 대비 상대 빈도 | $rel3 = \frac{\text{Bin mapped reads}}{\text{Total binned reads}}$ |

#### B. 품질 및 분류 정보 (Quality & Taxonomy)
테이블의 우측 끝 열에서 확인할 수 있는 정보입니다.

* **CheckM 결과 (Bin Quality)**
    * `Completeness`: 유전체 완성도
    * `Contamination`: 타 유전체 오염도
    * `Strain_heterogeneity`: 균주 균질성
    * `bin_quality`: 위 지표를 근거로 한 등급 (예: Near Complete = Completeness $\ge$ 90% & Contamination $<$ 5%)
* **GTDB_tk 결과 (Taxonomy)**
    * `Classification`: 각 Bin이 속하는 Taxa 정보
    * `ANI 관련 컬럼(2개)`: 해당 분류군(Classification)과의 ANI(Average Nucleotide Identity) 값

---

### ⚠️ 주의사항 (Caveats)
이 테이블에 포함된 데이터는 일반적인 샷건 메타유전체 분석 과정에서 발생할 수 있는 에러의 위험성 때문에 최종 결과물로 직접 사용하기에는 주의가 필요합니다. 하지만 **전체적인 분석의 흐름을 파악하고 데이터의 내러티브를 구성하는 데에는 충분히 활용 가능한 자료**입니다.
