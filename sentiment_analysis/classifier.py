from transformers import pipeline

# 감성 분류 파이프라인 로드 (최초 1회만 로딩됨)
classifier = pipeline("sentiment-analysis", model="snunlp/KR-FinBert-SC")

def classify_review(text: str) -> tuple[str, float]:
    """
    리뷰 텍스트를 받아 'positive' 또는 'negative' 및 확률 반환
    """
    result = classifier(text[:512])[0]  # 너무 긴 텍스트는 자름
    return result["label"].lower(), result["score"]
