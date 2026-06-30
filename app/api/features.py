from fastapi import APIRouter, HTTPException
from app.schemas.feature import FeatureRequest, FeatureResponse
from app.services.firebase import get_db

router = APIRouter()


@router.post("/features", response_model=FeatureResponse)
async def save_features(body: FeatureRequest):
    try:
        ref = get_db()
        key = f"features/{body.user_id}/{body.date}"
        data = {}
        if body.speech is not None:
            data["speech"] = body.speech.model_dump()
        if body.keystroke is not None:
            data["keystroke"] = body.keystroke.model_dump()
        if not data:
            raise HTTPException(status_code=400, detail="speech 또는 keystroke 중 하나는 필요합니다")
        ref.child(key).update(data)
        return FeatureResponse(
            status="ok",
            message="피처 저장 완료",
            saved_key=key,
        )
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Firebase 저장 실패: {e}")
