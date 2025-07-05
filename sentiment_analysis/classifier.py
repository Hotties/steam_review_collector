# analyze/classifier.py

from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from typing import Literal

# 긍정 또는 부정을 나타내는 타입 정의
Sentiment = Literal["positive", "negative"]

class SentimentClassifier:
    def __init__(self):
        model_name = "beomi/KcELECTRA-base"
        print("[INFO] Loading KcELECTRA model...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.classifier = pipeline("sentiment-analysis", model=self.model, tokenizer=self.tokenizer)
        print("[INFO] Model loaded.")

    def predict(self, text: str) -> Sentiment:
        result = self.classifier(text[:512])[0]  # 512 토큰 초과 방지
        label = result['label']
        
        # KcELECTRA는 보통 LABEL_0: 부정, LABEL_1: 긍정
        if label == 'LABEL_1':
            return "positive"
        else:
            return "negative"
