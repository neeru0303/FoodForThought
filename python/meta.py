import re


class Restaurant:
    def __init__(self, restaurantid, name, city, rating, items=['fries']):
        self.restaurantid = restaurantid
        self.name = name
        self.rating = rating
        self.city = city
        self.items = items


class Mention:
    def __init__(self, restaurant, reviewid, text, mention, sentiment):
        # print type(restaurant)
        pattern = re.compile(r"[^a-zA-Z0-9]+")
        self.restaurant = restaurant
        self.reviewid = reviewid
        self.text = text
        self.bfrmention = mention
        self.mention = pattern.sub(" ", mention)
        self.sentiment = sentiment.strip()
        self.items = []

    def addItem(self, item):
        self.items.append(item)
