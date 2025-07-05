from collect.collect_reviews import collect_reviews
from db.db import get_connection
from db.schema import create_reviews_table
from db.insert import insert_review



from sentiment_analysis.classifier import SentimentClassifier
from sentiment_analysis.schema import create_sentiment_tables
from sentiment_analysis.db_handler import insert_sentiment_review

def main():
    reviews = collect_reviews()
    if not reviews:
        print("[WARN] No reviews to process.")
        return
    classifier = SentimentClassifier()
    conn = get_connection()
    create_reviews_table(conn)
    create_sentiment_tables(conn)
    for r in reviews:
        try:
            c = classifier.predict(r.review)
            print(c)
            ##insert_review(conn, r)
        except Exception as e:
            print(f"[ERROR] Failed to insert review {r.review_id}: {e}")
    conn.close()

if __name__ == "__main__":
    main()
