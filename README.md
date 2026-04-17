# Sales Analytics Dashboard

Streamlit 기반 매출 분석 대시보드 프로젝트입니다.

## 주요 기능

- **사이드바 필터**: 날짜 범위, 지역, 제품별 필터링
- **KPI 카드 4개**: 총 매출(전월 대비 증감), 주문 건수, 평균 주문액, 최다 판매 제품
- **매출 추이 차트**: 월별 매출 추이 라인 차트 (Plotly)
- **제품별 차트**: 제품별 매출 막대 차트 (Plotly)
- **지역별 차트**: 지역별 매출 비중 파이 차트 (Plotly)
- **CSV 다운로드**: 필터링된 데이터를 CSV로 다운로드
- **원본 데이터 보기**: expander로 원본 테이블 확인

## 프로젝트 구조

```
├── app.py                # 메인 Streamlit 앱
├── data/
│   └── sales_data.csv    # 판매 데이터 (2024년)
├── utils/
│   ├── charts.py         # Plotly 차트 함수
│   └── filters.py        # 사이드바 필터 로직
└── requirements.txt      # 의존성 패키지
```

## 데이터 구조 (sales_data.csv)

| 컬럼 | 설명 |
|------|------|
| date | 날짜 (2024-01-01 ~ 2024-12-31) |
| product | 제품 (노트북, 스마트폰, 태블릿, 이어폰) |
| region | 지역 (서울, 부산, 대구, 인천, 광주) |
| quantity | 판매 수량 |
| sales | 판매 금액 (원) |

## 실행 방법

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 기술 스택

- **Python 3**
- **Streamlit** - 웹 대시보드 프레임워크
- **Pandas** - 데이터 처리
- **Plotly** - 인터랙티브 차트
