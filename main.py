from collect.collect_reviews import collect_reviews
from db.db import get_connection
from db.schema import create_reviews_table
from db.insert import insert_review

from sentiment_analysis.classifier import SentimentClassifier
from sentiment_analysis.schema import create_sentiment_tables
from sentiment_analysis.db_handler import insert_sentiment_review

from noun_frequency.noun_extractor import extract_nouns
from noun_frequency.chart_generator import plot_top_n_nouns

import time

def main():
    
    ##print(extract_nouns("점심으로 맛있는 짜장면과 탕수육을 먹었습니다. 배가 부르네요."))
    reviews = collect_reviews()
    if not reviews:
        print("[WARN] No reviews to process.")
        return
    classifier = SentimentClassifier()
    conn = get_connection()
    create_reviews_table(conn)
    create_sentiment_tables(conn)
    
    nouns = []

    for r in reviews:
        c = classifier.predict(r.review)
        try:
            print(c)
            if c == 'negative':
                nouns.append(extract_nouns(r.review)) 
        except Exception as e:
            print(f"[ERROR] Failed to insert review {r.review_id}: {e}")
        """
        try:
            print(2)
            insert_review(conn, r)
        except Exception as e:
            print()
        try:
            print(3)
            insert_sentiment_review(conn,r, c)
        except Exception as e:
            print()
        """
        time.sleep(5)
    conn.close()
    
    ##plot_top_n_nouns(nouns)


if __name__ == "__main__":
    main()
    