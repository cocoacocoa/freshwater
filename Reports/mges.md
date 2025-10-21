## Mobile Genetic Element Assignment

### Assignment result for Megahit assembly 0402_01

  - Assignment: geNomad on whole assembly (option: --cleanup --conservative --lenient-taxonomy --full-ictv-lineage)
  - 파일 위치: [root directory]/mges/genomad/assembly/total_assembly_megahit_0402_01/genomad_out_01
  - Plasmid로 assign된 assembly의 갯수(plasmid score > 0.8): 5,246개
  - Virus(provirus)로 assign된 assembly의 갯수(virus score > 0.8): 280,464개

#### Virus statistics and ChatGPT commment

  - 원본 파일 링크: []()
  - Top 20 most detected viruses

```
 209672 Viruses;Duplodnaviria;;Heunggongvirae;;Uroviricota;;Caudoviricetes;;;;;;;;
   8542 Viruses;Varidnaviria;;Bamfordvirae;;Nucleocytoviricota;;Megaviricetes;;Algavirales;;Phycodnaviridae;;;;
   7535 Unclassified
   7531 Viruses;Duplodnaviria;;Heunggongvirae;;Uroviricota;;Caudoviricetes;;;;Kyanoviridae;;;;
   6113 Viruses;Varidnaviria;;Bamfordvirae;;Nucleocytoviricota;;Megaviricetes;;Imitervirales;;Mimiviridae;;;;
   5573 Viruses;Varidnaviria;;Bamfordvirae;;Preplasmiviricota;;Maveriviricetes;;Priklausovirales;;;;;;
   3882 Viruses;Varidnaviria;;Bamfordvirae;;Nucleocytoviricota;;Megaviricetes;;;;;;;;
   3654 Viruses;Varidnaviria;;Bamfordvirae;;Nucleocytoviricota;;Megaviricetes;;Imitervirales;;;;;;
   2686 Viruses;Duplodnaviria;;Heunggongvirae;;Uroviricota;;Caudoviricetes;;;;Straboviridae;;;;
   2120 Viruses;Duplodnaviria;;Heunggongvirae;;Uroviricota;;Caudoviricetes;;;;Autographiviridae;;;;
   2037 Viruses;Varidnaviria;;Bamfordvirae;;Preplasmiviricota;;Polintoviricetes;;Orthopolintovirales;;Adintoviridae;;;;
   1867 Viruses;Duplodnaviria;;Heunggongvirae;;Uroviricota;;Caudoviricetes;;;;Stanwilliamsviridae;;;;
   1543 Viruses;Duplodnaviria;;Heunggongvirae;;Uroviricota;;Caudoviricetes;;;;Straboviridae;Tevenvirinae;;;
   1527 Viruses;Duplodnaviria;;Heunggongvirae;;Uroviricota;;Caudoviricetes;;;;Autographiviridae;Studiervirinae;;;
   1428 Viruses;Duplodnaviria;;Heunggongvirae;;Uroviricota;;Caudoviricetes;;;;;Beephvirinae;;;
   1179 Viruses;Varidnaviria;;Bamfordvirae;;Nucleocytoviricota;;Megaviricetes;;Imitervirales;;Mimiviridae;Megamimivirinae;;;
   1178 Viruses;Duplodnaviria;;Heunggongvirae;;Uroviricota;;Caudoviricetes;;Crassvirales;;;;;;
   1041 Viruses;Duplodnaviria;;Heunggongvirae;;Uroviricota;;Caudoviricetes;;;;Demerecviridae;Markadamsvirinae;;;
    816 Viruses;Varidnaviria;;Bamfordvirae;;Nucleocytoviricota;;Megaviricetes;;Algavirales;;Phycodnaviridae;;Prasinovirus;;
    649 Viruses;Duplodnaviria;;Heunggongvirae;;Uroviricota;;Caudoviricetes;;;;;;Bruynoghevirus;;
    638 Viruses;Varidnaviria;;Bamfordvirae;;Nucleocytoviricota;;Pokkesviricetes;;Chitovirales;;Poxviridae;Chordopoxvirinae;Avipoxvirus;;Avipoxvirus fowlpox
```

  - ChatGPT의 의견

```
꼬리박테리오파지(Caudoviricetes)의 우세
파지 풍부: 데이터는 카우도비리세테스 (꼬리 박테리오파지)의 존재를 압도적으로 보여줍니다. 이 그룹에서 20만 개 이상의 염기서열이 분류되었는데, 이는 파지가 바이러스 군집을 지배하고 있음을 시사합니다. 수생 환경에는 일반적으로 밀리리터당 10^7개의 바이러스 입자가 존재하며, 대부분이 박테리오파지이기 때문에 이러한 현상이 예상됩니다. 이 파지는 물 속 미생물 집단을 형성하는 주요 비리오플랑크톤 입니다.
새로운 파지 패밀리(키아노바이러스과 & 오토그라피바이러스과): 특히 많은 서열이 최근에 확립된 파지 패밀리에 속했습니다. 키아노바이러스과 (7,531개 서열)와 오토그라피바이러스과 (2,120개 서열)는 가장 풍부한 분류군에 속했습니다. 이는 전통적인 미오바이러스과(대형 수축꼬리 파지)와 포도바이러스과(짧은꼬리 파지)에 해당하며, ICTV에 의해 재분류되었습니다. Kyanoviridae는 많은 시아노파지 계통(시아노박테리아를 감염시키는 파지)을 포함하는데, 이는 강에 풍부한 시아노박테리아 숙주를 시사합니다. Autographiviridae는 T7 유사 용균 파지를 포함합니다. 실제로, 고전적인 대장균 파지인 T7 (테셉 티마바이러스 속)과 T4 유사 파지(스트라보바이러스과 테콰트로바이러스속)가 샘플에서 검출되었습니다. 이는 하수나 유출수를 통해 강으로 유입되는 일반적인 장내 박테리오파지(예: 대장균 감염 파지)의 존재를 확인합니다.
CrAssphage – 분변 오염 지표: Crassvirales 목( Suoliviridae 과) 의 염기서열 도 확인되었습니다(예: 약 220개). 이는 인간 장내 박테리오파지 그룹인 crAssphage 에 해당합니다. CrAssphage는 인간 분변 미생물군집에서 가장 흔한 바이러스 중 하나이며, 수중 인간 분변 오염의 유전적 지표로 널리 사용됩니다. crAssphage 관련 시퀀스의 감지는 인간의 하수 또는 유출수가 강의 바이롬에 영향을 미쳐 인간 장과 관련된 파지를 도입했음을 시사합니다. 이는 한강의 도시 환경과 관련이 있으며, 바이롬 분석을 통해 어떻게 분변 오염을 밝혀낼 수 있는지를 보여줍니다.

거대 바이러스와 비로파지
거대 바이러스(NCLDV): 박테리오파지 외에도 메타게놈에는 핵-세포질 거대 DNA 바이러스(NCLDV) 의 많은 염기서열이 포함되어 있으며, 이는 거대 바이러스라고도 불립니다. 예를 들어, 6,000개 이상의 염기서열이 미미 바이러스과(Mimiviridae)로 분류되었으며, 여기에는 미미바이러스, 메가바이러스, 그리고 이와 관련된 거대 바이러스들이 포함됩니다. 이들은 자유 생활 아메바와 기타 원생생물을 감염시킵니다. 미미바이러스과에 속하는 거대 바이러스는 자연수에서 자주 발견되며, 그중 다수는 호수, 강, 바다와 같은 수생 환경에서 분리되었습니다. 한강 표본에서 이들의 존재는 놀라운 일이 아니며, 풍부한 원생생물(아메바) 개체군이 숙주 역할을 한다는 것을 시사합니다. 알로미미 바이러스과(Allomimiviridae)와 클로스노이비리나에(Klosneuvirinae)와 같은 아과(예: 테이아바이러스속(Theiavirus))를 포함한 다른 NCLDV 과(family)들도 검출되었는데, 이는 환경 메타게놈에서 새롭게 발견된 거대 바이러스 계통을 나타냅니다.
바이로파지(스푸트니크바이러스): 특히 흥미로운 발견은 바이로파지 서열 의 검출입니다 . 약 31개의 서열이 스푸트니크바이러스(라비다바이러스과, 스푸트니비로바이러스과* 라고도 함)로 분류되었습니다. 스푸트니크 바이로파지는 거대 바이러스 에 기생하는 작은 바이러스로, 같은 숙주 아메바를 동시에 감염시켜 거대 바이러스의 복제 메커니즘을 장악합니다. 최초의 바이로파지인 스푸트니크는 원래 미미바이러스와 함께 아메바를 감염시키는 것으로 발견되었습니다. 샘플에서 스푸트니크 유사 바이로파지 DNA가 발견된 것은 미미바이러스와 같은 거대 바이러스가 강에서 숙주를 활발하게 감염시키고 있다는 강력한 증거입니다. 왜냐하면 바이로파지는 이러한 동시 감염에 의존하기 때문입니다. 본질적으로 한강 생태계는 거대 바이러스뿐만 아니라 이러한 "바이러스 중의 바이러스"도 포함하고 있으며, 이는 미생물 먹이 사슬에서 바이러스-숙주-바이러스 간의 복잡한 상호작용을 강조합니다.

조류 바이러스(Phycodnaviridae 및 관련 바이러스)
피코드나바이러스과(Phycodnaviridae) (조류 dsDNA 바이러스): 바이러스 DNA의 상당 부분이 피코드나 바이러스과에 속하는 것으로 밝혀졌으며, 총 약 8,542개의 염기서열을 가지고 있습니다. 피코드나바이러스는 조류(식물성 플랑크톤)를 감염시키는 대형 정이십면체 dsDNA 바이러스입니다. 전 세계 담수와 해수에 널리 분포 하며 , 조류 대발생 시기에는 높은 농도에 도달하는 경우가 많습니다. 여기에서 높은 빈도로 나타나는 것은 한강에서 조류의 활발한 감염을 시사합니다. 이러한 바이러스는 조류 개체군 역학을 조절하여 수질과 영양염 순환에 영향을 미칠 수 있습니다.
클로로바이러스와 프라시노바이러스: 피코드나 바이러스과(Phycodnaviridae) 내에서 특정 속(genus)이 검출되었습니다. 특히 클로로바이러스 (618개 염기서열)가 확인되었습니다. 클로로바이러스는 담수 호수와 강에서 흔히 발견되는 특정 단세포 녹조류( 클로렐라 종 등)를 감염시킵니다. 예를 들어, PBCV-1 과 같은 클로렐라 바이러스는 이 속(genus)에서 잘 연구된 바이러스입니다. 이 바이러스들은 조류 세포벽에 부착하여 숙주를 빠르게 용해시켜 자손을 물속으로 방출할 수 있습니다. 이 샘플에는 또한 프라시노바이러스 염기서열(약 816개 히트)이 포함되어 있는데, 이는 피코플랑크톤 녹조류(프라시노파이트)를 감염시키는 바이러스에 해당합니다. 프라시노바이러스는 일반적으로 해양 녹조류(예: 오스트레오코쿠스 )를 표적으로 삼지만, 연안 및 하구 수역에서도 관련 바이러스가 발견되었습니다. 이러한 바이러스의 존재는 해양 영향(하류 하구 유입) 또는 하천 내 프라시노파이트 조류의 담수 친척 감염을 시사할 수 있습니다. 전반적으로 조류 바이러스의 풍부함은 하천 내 진핵 플랑크톤 의 다양성을 강조하며 , 조류에서 바이러스에 의한 사망률을 보여줍니다.

병원성 척추동물 바이러스 검출
원숭이두 바이러스(오르토폭스바이러스): 놀라운 발견 중 하나는 원숭이두 바이러스 (mpox) 로 분류되는 약 67개의 염기서열이었습니다 . 원숭이두는 2022년에서 2023년 사이에 사람에게 발병을 일으킨 인수공통전염병 바이러스( 오르토폭스바이러스 속 )입니다. 수질 시료에서 발견된 이 바이러스의 DNA는 주목할 만합니다. 원숭이두 바이러스는 환경적으로 안정한 것으로 알려진 크고 이중 가닥 DNA 바이러스입니다. 실제로 연구에 따르면 원숭이두 바이러스는 염소 처리되지 않은 물과 폐수에서 몇 주 동안 생존 할 수 있습니다. 예를 들어, 최근 실험에서는 처리되지 않은 물에서 MPXV가 지속되는 것으로 나타났으며, 이는 하수를 통한 바이러스 확산에 대한 우려를 불러일으켰습니다. 한강에서 원숭이두창 DNA가 검출된 것은 발병 기간 중 오염된 폐수 방류 때문일 수 있습니다. 원숭이두창 DNA의 유전 물질 존재가 전염성 바이러스의 존재를 확증하는 것은 아니지만, 인간의 병원균이 어떻게 환경 수역으로 유입될 수 있는지를 보여줍니다.
아프리카돼지열병 바이러스(아스파바이러스과): 아프리카돼지열병 바이러스 (ASFV) 로 확인된 6개의 염기서열이 있습니다 . ASFV는 돼지와 야생 멧돼지를 감염시켜 돼지에게 심각한 출혈열을 유발하는 경제적으로 중요한 병원체입니다. 외피를 가진 이중 DNA 바이러스( 아스파 바이러스과 )이며, 환경에서 매우 강력한 것으로 알려져 있습니다. 특히, ASFV는 서늘한 수온에서 6주 이상 강물에서 안정적으로 감염력을 유지할 수 있습니다. 예를 들어, 한 연구에서는 ASFV가 4°C 물에서 42일 이상 생존한다는 사실을 발견했습니다. 강에서 ASFV DNA가 검출된 것은 돼지 농장 폐수, 도축장 폐기물, 또는 부패 중인 야생 멧돼지 사체와 같은 상류 오염원에서 유래되었을 가능성이 있습니다. 이러한 DNA의 존재는 질병 확산의 잠재적 경로(예: 수인성 전파 또는 하류를 통한 사체 이동)를 시사하므로 중요한 생물안전 신호입니다.
아비폭스바이러스(계두): 또 다른 주목할 만한 분류군은 계두 바이러스 (폭스바이러스과 (Poxviridae)의 아비폭스바이러스 속 )로, 약 638개의 염기서열을 가지고 있습니다. 계두는 가금류와 야생 조류를 감염시켜 병변을 유발하고, 이 병변은 바이러스가 묻은 딱지를 환경으로 배출할 수 있습니다. 계두와 같은 계두바이러스는 내한성이 강합니다. 예를 들어, 관련 우두 바이러스는 환경 수역에서 생존하는 것으로 나타났습니다(한 보고서에 따르면 우두 바이러스는 우수와 분변에서 장기간 생존했습니다). 따라서 강 주변의 감염된 조류(또는 오염된 가금류 사육 유출수)가 물에 가금두 바이러스 DNA를 유입시켰을 가능성이 있습니다. 조류두 바이러스 염기서열의 검출은 동물 질병 이 환경 메타게놈에 유전적 특징을 어떻게 남길 수 있는지를 보여줍니다. 이러한 바이러스는 인간에게 직접적인 위험을 초래하지는 않지만, 환경 모니터링은 수의 역학 연구에 유용할 수 있습니다.

결론
요약하자면, 한강 바이롬에는 박테리오파지의 우점종으로 예상되는 것부터 거대 조류 바이러스, 심지어 주요 동물 바이러스의 DNA까지 매우 다양한 바이러스가 포함되어 있습니다. 시아노파지와 T7/T4 유사 파지 (키아노바이러스과, 오토그라피바이러스과)의 풍부한 존재는 활발한 박테리아 생태계를 반영하는 반면, 크라스파지 의 존재는 인간의 분변 오염을 시사합니다. 거대 아메바 감염 바이러스 (Mimiviridae)와 그 스푸트니크 비로파지 의 검출은 물 속 바이러스-숙주 상호 작용의 복잡성을 보여줍니다. 한편, 오르토폭스바이러스와 아스파바이러스 DNA 발견은 환경 시료에서 바이러스 병원균을 추적할 수 있음을 보여주며, 이는 인간, 동물, 그리고 환경 건강 간의 원헬스(One Health) 연관성을 강조합니다. 이러한 각 분류군은 하천 미생물 군집의 생태적 및 공중보건적 맥락을 이해하는 데 중요한 단서를 제공합니다. 문헌에 뒷받침되는 메타게놈학적 증거는 미생물뿐만 아니라 그 생명체를 잡아먹는(그리고 때로는 공생하는) 바이러스로 가득 찬 하천의 모습을 보여줍니다.
```

#### Plasmid statistics


