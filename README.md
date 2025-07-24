# 📦 Steam Review Collector

**Steam Review Collector**는 Steam 게임 리뷰를 수집하고, 감정 분석 및 단어 빈도 분석을 통해 인사이트를 시각화하는 파이프라인 프로젝트입니다.

---

## 🔧 기능

- ✅ Steam 게임 리뷰 수집 및 저장
- ✅ 리뷰 데이터의 명사 추출 및 시각화
- ✅ 감성 분석 (긍정/부정 분류)
- ✅ SQLite 기반 로컬 데이터베이스 저장

---

## 🗂️ 프로젝트 구조

```
steam_review_collector/
│
├── main.py                         # 메인 실행 파일
├── data/                           # 수집된 리뷰 JSON 파일 저장
├── db/                             # DB 연결 및 삽입 로직
│   ├── db.py
│   ├── insert.py
│   └── schema.py
├── model/                          # 리뷰 데이터 모델 정의
│   └── review.py
├── noun_frequency/                # 명사 추출 및 시각화
│   ├── noun_extractor.py
│   └── chart_generator.py
└── sentiment_analysis/           # 감성 분석 로직
    ├── classifier.py
    ├── db_handler.py
    └── schema.py
```

---

## 🚀 실행 방법

```bash
# 의존성 설치 (예: requirements.txt가 있다면)
pip install -r requirements.txt

# setup.py 실행
python setup.py install

# 프로젝트 실행
python main.py
```

---

## 📊 결과 예시

- 리뷰의 감정 분석 결과 출력
- 리뷰에서 단어 추출

---

## 📌 사용 기술

- Python 3.x
- SQLite
- KoNLPy / Okt (형태소 분석기)
- Matplotlib
- Scikit-learn (감성 분석)

---

## 📁 향후 개선점

- 문장에 따른 감정 분석 개선

