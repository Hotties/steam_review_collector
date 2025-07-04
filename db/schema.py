
import pymysql

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS steam_reviews (
    review_id BIGINT PRIMARY KEY,
    steamid BIGINT,
    playtime_at_review INT,
    playtime_forever INT,
    review TEXT,
    language VARCHAR(20),
    voted_up BOOLEAN,
    timestamp_created DATETIME,
    steam_purchase BOOLEAN
);
"""

# steam_review_collector/schema.py

def create_reviews_table(conn):
    with conn.cursor() as cursor:
        cursor.execute(CREATE_TABLE_SQL)
    conn.commit()
    print("[INFO] Table 'steam_reviews' ensured.")
    
