def insert_sentiment_review(conn, review, sentiment: str, score: float):
    with conn.cursor() as cursor:
        if sentiment == 'positive':
            cursor.execute("""
                INSERT INTO positive_reviews (recommendationid, steamid, positive_score, steam_purchase)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE positive_score = VALUES(positive_score)
            """, (review.review_id, review.steamid, score, review.steam_purchase))
        elif sentiment == 'negative':
            cursor.execute("""
                INSERT INTO negative_reviews (recommendationid, steamid, negative_score, steam_purchase)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE negative_score = VALUES(negative_score)
            """, (review.review_id, review.steamid, score, review.steam_purchase))
    conn.commit()
