#!/usr/bin/env python

import re


class Restaurant:
    def __init__(self, restaurant_id, name, city, rating, items=['fries']):
        self.restaurant_id = restaurant_id
        self.name = name
        self.rating = rating
        self.city = city
        self.items = items


class Mention:
    def __init__(self, restaurant, reviewid, text, mention, sentiment):
        # print type(restaurant)
        pattern = re.compile(r"[^a-zA-Z0-9]+")
        self.restaurant = restaurant
        self.review_id = reviewid
        self.review_text = text
        self.bfrmention = mention
        self.mention_text = pattern.sub(" ", mention)
        self.sentiment = sentiment.strip()
        self.items = []

    def add_item(self, item):
        self.items.append(item)
