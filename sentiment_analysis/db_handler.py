def insert_sentiment_review(conn, review, sentiment: str):
    with conn.cursor() as cursor:
        if sentiment == 'positive':
            print(f"{sentiment}")
            cursor.execute("""
                INSERT INTO positive_reviews (recommendationid, steamid, sentiment, steam_purchase)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE sentiment = VALUES(sentiment)
            """, (review.review_id, review.steamid,sentiment, review.steam_purchase))
        elif sentiment == 'negative':
            print(f"{sentiment}")
            cursor.execute("""
                INSERT INTO negative_reviews (recommendationid, steamid, sentiment, steam_purchase)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE sentiment = VALUES(sentiment)
            """, (review.review_id, review.steamid, sentiment, review.steam_purchase))
    conn.commit()
