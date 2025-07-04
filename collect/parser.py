import json
import os
from model.review import SteamReview
def load_reviews_from_json_file(app_id: str) -> list[SteamReview]:
    path = f"./data/review_{app_id}.json"
    if not os.path.exists(path):
        print(f"[ERROR] JSON file not found: {path}")
        return []

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    raw_reviews = data.get("reviews", {})
    reviews = []

    for review_id, review_data in raw_reviews.items():
        try:
            reviews.append(SteamReview(review_data))
        except Exception as e:
            print(f"[ERROR] Failed to parse review {review_id}: {e}")
    
    return reviews
