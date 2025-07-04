import steamreviews
import os

def fetch_reviews(app_id: str) -> dict:
    request_params = {
        'language': 'korean',
        'purchase_type': 'steam'
    }
    review_dict, _ = steamreviews.download_reviews_for_app_id(
        app_id, query_count=1, chosen_request_params=request_params
    )

    output_path = f"./data/review_{app_id}.json"
    os.makedirs("data", exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        import json
        json.dump(review_dict, f, indent=2, ensure_ascii=False)

    return review_dict
