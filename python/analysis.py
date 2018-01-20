from __future__ import division
import match
import json
import sys

from meta import Restaurant, Mention

reload(sys)
sys.setdefaultencoding('utf8')

restaurants = {}
mentions = {}


def read_restaurant_data():
    with open("data/restuarants.json") as restaurant:
        for i in restaurant.readlines():
            try:
                i = json.loads(i)
                restaurants[i["business_id"]] = Restaurant(i["business_id"], i["name"], i["city"], i["stars"],
                                                           i.get("items", []))
            # print i["business_id"],i["name"],i["city"],i["stars"]
            except:
                pass

            # print restuarants


def write_item_mention(x):
    with open("data/mentionWithItems.txt", x) as file_mention:
        for i in mentions:
            if len(mentions[i].items) != 0:
                mention = mentions[i]
                file_mention.write(
                    mention.restaurant.restaurantid + "~" + mention.reviewid + "~" + mention.mention + "~" + mention.sentiment + "~" + "-".join(
                        mention.items))
                file_mention.write("\n")


def read_mentions_data():
    with open("data/mention.txt") as mention:
        for i in mention.readlines():
            i = i.split("~")
            try:
                # print len(i)
                mentions[i[1]] = Mention(restaurants[i[0]], i[1], i[2], i[3], i[4])
            # print type(mentions[i[1]].restaurant.items)
            except:
                pass


read_restaurant_data()
read_mentions_data()
# print type(mentions['apzxETosswLEoNIwHOh7nA'].restaurant)
exact_match = match.ExactMatcher()
exact_match.matcher(mentions)
write_item_mention('w')
partial_match = match.PartialMatcher()
partial_match.matcher(mentions)
print mentions['Ht3HiWbSPbzAJ7TnQJtKhQ'].bfrmention
print mentions['Ht3HiWbSPbzAJ7TnQJtKhQ'].mention
print mentions['VmB6OWKb10tEy8o9EyNzYw'].items
print restaurants['N5dkbfyNWZPxOMWDiJp7TQ'].items
write_item_mention('a')
substring_match = match.SubStringMatcher()
substring_match.matcher(mentions)
write_item_mention('a')
fuzzy_match = match.FuzzyMatcher()
fuzzy_match.matcher(mentions)
write_item_mention('a')

"""
exactmatch = Match.ExactMatcher()
with open("data/mention.txt") as mention:
	x=exactmatch.matcher(mention.readlines())
	if x is not None:
		print x
"""
