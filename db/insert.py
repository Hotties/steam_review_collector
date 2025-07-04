def insert_review(conn, review):
    sql = """
    INSERT INTO steam_reviews
    (review_id, steamid, playtime_at_review, playtime_forever, review,
    language, voted_up, timestamp_created, steam_purchase)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    review = VALUES(review),
    voted_up = VALUES(voted_up),
    timestamp_created = VALUES(timestamp_created),
    steam_purchase = VALUES(steam_purchase),
    playtime_at_review = VALUES(playtime_at_review),
    playtime_forever = VALUES(playtime_forever)
    """
    with conn.cursor() as cursor:
        cursor.execute(sql, (
            review.review_id,
            review.steamid,
            review.playtime_at_review,
            review.playtime_forever,
            review.review,
            review.language,
            review.voted_up,
            review.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            review.steam_purchase
        ))
    conn.commit()
