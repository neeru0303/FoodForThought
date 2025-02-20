#!/usr/bin/env python
"""
Module used to define Restraurant and Mention Types
"""


import re


class Restaurant(object):
    """
    Class for restaurant data
    """

    def __init__(self, restaurant_id, name, city, rating, items=None):
        self.restaurant_id = restaurant_id
        self.name = name
        self.rating = rating
        self.city = city
        self.items = items if items else ["Fries"]



class Mention(object):
    """
    Class for Mention data
    """
    def __init__(self, restaurant, review_id, review_text, mention_text, sentiment):
        # print type(restaurant)
        pattern = re.compile(r"[^a-zA-Z0-9]+")
        self.restaurant = restaurant
        self.review_id = review_id
        self.review_text = review_text
        self.bfrmention = mention_text
        self.mention_text = pattern.sub(" ", mention_text)
        self.sentiment = sentiment.strip()
        self.items = []

    def add_item(self, item):
        """
        method to add restaurant items to mention
        :param item:
        :return:
        """
        self.items.append(item)

