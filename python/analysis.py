#!/usr/bin/env python
"""
driver program to perform match of restaurant items and mentions in an review
"""
from __future__ import division
from __future__ import absolute_import
import sys
import json
import logging
import re
import match
from meta import Restaurant, Mention

reload(sys)
sys.setdefaultencoding('utf8')

restaurants = {}
mentions = {}


def read_restaurant_data():
    """
    Read restaurant data to generate Restaurant meta
    :return:
    """
    with open("data/restuarants.json") as restaurants_data:
        for restaurant in restaurants_data.readlines():
            try:
                # print re.match(r'^\s*$', restaurant).groups()
                restaurant = json.loads(restaurant)
                restaurants[restaurant["business_id"]] = Restaurant(restaurant["business_id"], restaurant["name"],
                                                                    restaurant["city"], restaurant["stars"],
                                                                    restaurant.get("items", []))
            # print i["business_id"],i["name"],i["city"],i["stars"]
            except ValueError:
                logger.error("Unable to parse data  {}".format(restaurant))
            except Exception as e:
                logger.error("Read restaurant failed because of {} ".format(e))


def write_item_mention(mode="w"):
    """
    Save mention data with match
    :param mode: w = Write or a = Append
    :return:
    """
    with open("data/mentionWithItems.txt", mode=mode) as file_mention:
        for restaurant, mention in mentions.items():
            if len(mention.items) != 0:
                file_mention.write("{restaurant_name}~{restaurant_items}~{review_id}~{review_text}~"
                                   "{mention_text}~{sentiment} \n".format(restaurant_name=mention.restaurant.name,
                                                                          restaurant_items="-".join(
                                                                              mention.restaurant.items),
                                                                          review_text=mention.review_text,
                                                                          sentiment=mention.sentiment,
                                                                          review_id=mention.review_id,
                                                                          mention_text=mention.mention_text)
                                   )


def read_mentions_data():
    """
    read mention data before match
    :return:
    """
    with open("data/mention.txt") as mentions_data:
        for mention in mentions_data.readlines():
            mention = mention.split("~")
            try:
                # print len(i)
                mentions[mention[1]] = Mention(restaurants[mention[0]], mention[1], mention[2], mention[3], mention[4])
            # print type(mentions[i[1]].restaurant.items)
            except KeyError:
                logger.debug(" Key not found for mention {}".format(mention[1]))


if __name__ == "__main__":

    try:
        logger = logging.getLogger("Mention Analysis")
        file_handler = logging.FileHandler("logs/analysis.log", mode="w")
        format_handler = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(format_handler)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)

        logger.info("Read restaurant data")
        read_restaurant_data()
        logger.info("Read mention data")
        read_mentions_data()

        logger.info("Start exact match")
        exact_match = match.ExactMatcher()
        exact_match.matcher(mentions)
        write_item_mention(mode='w')

        logger.info("Start partial match")
        partial_match = match.PartialMatcher()
        partial_match.matcher(mentions)
        write_item_mention(mode='a')

        logger.info("Start substring match")
        substring_match = match.SubStringMatcher()
        substring_match.matcher(mentions)
        write_item_mention(mode='a')

        logger.info("Start fuzzy match")
        fuzzy_match = match.FuzzyMatcher()
        fuzzy_match.matcher(mentions)
        write_item_mention(mode='a')

        logger.info("Analysis is successfully completed")

    except Exception as e:
        logger.error("Analysis failed because of {}".format(e))
