def create_sentiment_tables(conn):
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS positive_reviews (
                recommendationid BIGINT PRIMARY KEY,
                steamid BIGINT,
                sentiment VARCHAR(20),
                steam_purchase BOOLEAN
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS negative_reviews (
                recommendationid BIGINT PRIMARY KEY,
                steamid BIGINT,
                sentiment VARCHAR(20),
                steam_purchase BOOLEAN
            );
        """)
    conn.commit()
