from pydantic import BaseModel, Field
from typing import Optional


class SpeechFeatures(BaseModel):
    speaking_rate: float = Field(..., description="발화 속도 (음절/초)")
    pause_frequency: float = Field(..., description="휴지 빈도 (회/문장)")
    pause_duration: float = Field(..., description="평균 휴지 길이 (ms)")
    repetition_ratio: float = Field(..., description="반복 표현 비율 (0~1)")
    sentence_complexity: float = Field(..., description="문장 복잡도")


class KeystrokeFeatures(BaseModel):
    inter_key_interval: float = Field(..., description="키 입력 간격 (ms)")
    word_pause_duration: float = Field(..., description="단어 사이 휴지 (ms)")
    correction_time: float = Field(..., description="오타 수정 소요 시간 (ms)")
    chars_per_minute: float = Field(..., description="분당 입력 문자 수")


class FeatureRequest(BaseModel):
    user_id: str = Field(..., description="Firebase UID")
    date: str = Field(..., description="측정 날짜 (YYYY-MM-DD)")
    speech: Optional[SpeechFeatures] = None
    keystroke: Optional[KeystrokeFeatures] = None


class FeatureResponse(BaseModel):
    status: str
    message: str
    saved_key: str
