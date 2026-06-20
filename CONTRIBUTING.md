# 기여 가이드

## 브랜치 전략

```
main        ← 발표/배포용 (PR + 리뷰 1명 필수)
  └── develop  ← 팀 통합 브랜치 (PR 대상)
        ├── feature/기능명
        ├── fix/버그명
        └── chore/작업명
```

예시: `feature/whisper-pipeline`, `fix/lstm-inference-error`

## 커밋 컨벤션

```
feat: Whisper STT 음성 분석 파이프라인 추가
fix: LSTM 추론 서버 응답 오류 수정
chore: requirements.txt 의존성 추가
docs: API 명세 업데이트
refactor: 피처 추출 모듈 분리
style: 코드 포맷팅 정리
test: 피처 벡터 생성 유닛 테스트 추가
```

## PR 규칙

1. `develop` 브랜치로 PR 생성
2. PR 제목도 커밋 컨벤션 형식으로
3. 리뷰어 최소 1명 지정
4. `.env` 파일이 커밋에 포함되지 않았는지 확인
5. 모델 파일(`.pt`, `.pth`)은 커밋하지 않고 별도 공유

## 이슈 규칙

- 작업 시작 전 이슈 먼저 생성
- 커밋/브랜치에 이슈 번호 연결: `feat: 9차원 피처 API 구현 (#3)`
- 라벨 필수 지정
