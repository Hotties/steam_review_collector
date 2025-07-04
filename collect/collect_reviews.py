import os
from dotenv import load_dotenv

from collect.downloader import fetch_reviews
from collect.parser import load_reviews_from_json_file

def collect_reviews() -> list:
    """
    다운로드 및 JSON 파싱까지 수행한 리뷰 리스트 반환
    """
    load_dotenv()
    app_id = os.getenv("Tekken8_appId")
    if not app_id:
        raise ValueError("App ID not found in .env")

    print("[INFO] Downloading reviews...")
    _ = fetch_reviews(app_id)

    print("[INFO] Parsing reviews...")
    return load_reviews_from_json_file(app_id)
