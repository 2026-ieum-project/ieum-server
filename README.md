# ieum-server

> 이음(ツナグ) 추론 서버 — 음성·키스트로크 분석 및 LSTM 변화 점수 산출

**2026 글로벌 피우다프로젝트** | [이음 Android 레퍼지토리](https://github.com/2026-ieum-project/ieum-android)

---

## 주요 기능

- **음성 분석 파이프라인** — Whisper STT → 발화 속도·휴지·반복 표현·문장 복잡도·TTR 산출
- **9차원 피처 벡터 API** — 앱으로부터 일별 피처 벡터(9개 숫자) 수신
- **LSTM 변화 점수 산출** — 개인 베이스라인 대비 인지 변화 점수 계산
- **피처 정규화 / 결측치 처리**

## 분석 지표

| 채널 | 지표 |
|---|---|
| 음성 (5개) | 발화 속도, 휴지 빈도/길이, 어휘 다양성(TTR), 반복 표현 비율, 문장 복잡도 |
| 키스트로크 (4개) | 문자 입력 간격, 단어 사이 휴지, 오타 수정 소요 시간, 분당 입력 문자 수 |

## 기술 스택

| 항목 | 기술 |
|---|---|
| 언어 | Python 3.10+ |
| 서버 프레임워크 | Flask / FastAPI |
| 모델 | PyTorch (LSTM) |
| 음성 분석 | OpenAI Whisper API |
| 형태소 분석 | KoNLPy (한국어), MeCab (일본어) |

## 개발 환경 설정

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

환경 변수 설정:
```bash
cp .env.example .env
# .env에 OPENAI_API_KEY 등 입력
```

서버 실행:
```bash
uvicorn app.main:app --reload   # FastAPI
# 또는
flask run                        # Flask
```

## 기여하기

[CONTRIBUTING.md](./CONTRIBUTING.md) 참고
