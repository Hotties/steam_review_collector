from datetime import datetime

class SteamReview:
    def __init__(self, data):
        author = data.get("author", {})
        self.review_id = int(data["recommendationid"])
        self.steamid = str(author.get("steamid"))
        self.playtime_at_review = int(author.get("playtime_at_review",0))
        self.playtime_forever = int(author.get("playtime_forever", 0))
        self.review = data.get("review", "")
        self.language = data.get("language", "all")
        self.voted_up = bool(data["voted_up"])
        self.timestamp = datetime.fromtimestamp(data["timestamp_created"])
        self.steam_purchase = bool(data["steam_purchase"])
