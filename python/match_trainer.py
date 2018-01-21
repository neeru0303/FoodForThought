from __future__ import unicode_literals
import spacy
from spacy.matcher import Matcher as Spacy_Matcher

import re
import os
import json
import sys
import logging
import argparse

reload(sys)
sys.setdefaultencoding('utf8')

nlp = spacy.load('en')
base_path = os.getcwd()
data_path = os.path.join(base_path, "data")
matcher_index = 1


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--log_level", "-l", help="log level", default="INFO")
    args = parser.parse_args()
    return args


def merge_phrases(matcher, doc, i, matches):
    '''
    Merge a phrase. We have to be careful here because we'll change the token indices.
    To avoid problems, merge all the phrases once we're called on the last match.
    '''
    if i != len(matches) - 1:
        return None
    spans = [(ent_id, label, doc[start: end]) for ent_id, label, start, end in matches]
    for ent_id, label, span in spans:
        span.merge('NNP' if label else span.root.tag_, span.text, nlp.vocab.strings[label])


def get_food_mentions(matcher, text):
    x = text.lower()
    x = nlp(x)
    try:
        matcher(x)
    except:
        pass
    s = ""
    for ent in x:

        if ent.ent_type_ == 'FOOD':
            # print ent,type(ent.string)
            # print dir(ent)
            s += ent.text + " "
    return s.encode('ascii', 'ignore')


def create_matcher(matcher, line):
    global matcher_index
    line = re.split(r'\W', line)
    line_length = len(line)
    if line_length == 1:
        # print line
        matcher_index += 1
        matcher.add(entity_key=str(matcher_index), label='FOOD', attrs={}, specs=[[{spacy.attrs.LOWER: line[0]}]],
                    on_match=merge_phrases)
        matcher_index += 1
        matcher.add(entity_key=str(matcher_index), label='FOOD', attrs={},
                    specs=[[{spacy.attrs.LOWER: line[0]}, {spacy.attrs.IS_PUNCT: True}]], on_match=merge_phrases)

    elif line_length == 2:
        matcher_index += 1
        matcher.add(entity_key=str(matcher_index), label='FOOD', attrs={},
                    specs=[[{spacy.attrs.LOWER: line[0]}, {spacy.attrs.LOWER: line[1]}]], on_match=merge_phrases)
        matcher_index += 1
        matcher.add(entity_key=str(matcher_index), label='FOOD', attrs={},
                    specs=[[{spacy.attrs.LOWER: line[0]}, {spacy.attrs.LOWER: line[1]}, {spacy.attrs.IS_PUNCT: True}]],
                    on_match=merge_phrases)
    elif line_length == 3:
        matcher_index += 1
        # print line
        matcher.add(entity_key=str(matcher_index), label='FOOD', attrs={},
                    specs=[[{spacy.attrs.LOWER: line[0]}, {spacy.attrs.LOWER: line[1]}, {spacy.attrs.LOWER: line[2]}]],
                    on_match=merge_phrases)
        matcher_index += 1
        matcher.add(entity_key=str(matcher_index), label='FOOD', attrs={}, specs=[
            [{spacy.attrs.LOWER: line[0]}, {spacy.attrs.LOWER: line[1]}, {spacy.attrs.LOWER: line[2]},
             {spacy.attrs.IS_PUNCT: True}]], on_match=merge_phrases)
    elif line_length == 4:
        matcher_index += 1
        # print line
        matcher.add(entity_key=str(matcher_index), label='FOOD', attrs={}, specs=[
            [{spacy.attrs.LOWER: line[0]}, {spacy.attrs.LOWER: line[1]}, {spacy.attrs.LOWER: line[2]},
             {spacy.attrs.LOWER: line[3]}]], on_match=merge_phrases)
        matcher_index += 1
        matcher.add(entity_key=str(matcher_index), label='FOOD', attrs={}, specs=[
            [{spacy.attrs.LOWER: line[0]}, {spacy.attrs.LOWER: line[1]}, {spacy.attrs.LOWER: line[2]},
             {spacy.attrs.LOWER: line[3]},
             {spacy.attrs.IS_PUNCT: True}]], on_match=merge_phrases)

    elif line_length == 5:
        matcher_index += 1
        # print line
        matcher.add(entity_key=str(matcher_index), label='FOOD', attrs={}, specs=[
            [{spacy.attrs.LOWER: line[0]}, {spacy.attrs.LOWER: line[1]}, {spacy.attrs.LOWER: line[2]},
             {spacy.attrs.LOWER: line[3]},
             {spacy.attrs.LOWER: line[4]}]], on_match=merge_phrases)
    elif line_length == 6:
        matcher_index += 1
        # print line
        matcher.add(entity_key=str(matcher_index), label='FOOD', attrs={}, specs=[
            [{spacy.attrs.LOWER: line[0]}, {spacy.attrs.LOWER: line[1]}, {spacy.attrs.LOWER: line[2]},
             {spacy.attrs.LOWER: line[3]},
             {spacy.attrs.LOWER: line[4]}, {spacy.attrs.LOWER: line[5]}]], on_match=merge_phrases)
    elif line_length == 7:
        matcher_index += 1
        # print line
        matcher.add(entity_key=str(matcher_index), label='FOOD', attrs={}, specs=[
            [{spacy.attrs.LOWER: line[0]}, {spacy.attrs.LOWER: line[1]}, {spacy.attrs.LOWER: line[2]},
             {spacy.attrs.LOWER: line[3]}, \
             {spacy.attrs.LOWER: line[4]}, {spacy.attrs.LOWER: line[5]}, {spacy.attrs.LOWER: line[6]}]],
                    on_match=merge_phrases)
    elif line_length == 8:
        matcher_index += 1
        # print line
        matcher.add(entity_key=str(matcher_index), label='FOOD', attrs={}, specs=[
            [{spacy.attrs.LOWER: line[0]}, {spacy.attrs.LOWER: line[1]}, {spacy.attrs.LOWER: line[2]},
             {spacy.attrs.LOWER: line[3]}, \
             {spacy.attrs.LOWER: line[4]}, {spacy.attrs.LOWER: line[5]}, {spacy.attrs.LOWER: line[6]},
             {spacy.attrs.LOWER: line[7]}]], on_match=merge_phrases)
    elif line_length == 9:
        matcher_index += 1
        # print line
        matcher.add(entity_key=str(matcher_index), label='FOOD', attrs={}, specs=[
            [{spacy.attrs.LOWER: line[0]}, {spacy.attrs.LOWER: line[1]}, {spacy.attrs.LOWER: line[2]},
             {spacy.attrs.LOWER: line[3]}, \
             {spacy.attrs.LOWER: line[4]}, {spacy.attrs.LOWER: line[5]}, {spacy.attrs.LOWER: line[6]},
             {spacy.attrs.LOWER: line[7]},
             {spacy.attrs.LOWER: line[8]}]], on_match=merge_phrases)
    elif line_length >= 10:
        matcher_index += 1
        # print line
        matcher.add(entity_key=str(matcher_index), label='FOOD', attrs={}, specs=[
            [{spacy.attrs.LOWER: line[0]}, {spacy.attrs.LOWER: line[1]}, {spacy.attrs.LOWER: line[2]},
             {spacy.attrs.LOWER: line[3]}, \
             {spacy.attrs.LOWER: line[4]}, {spacy.attrs.LOWER: line[5]}, {spacy.attrs.LOWER: line[6]},
             {spacy.attrs.LOWER: line[7]},
             {spacy.attrs.LOWER: line[8]}]], on_match=merge_phrases)
    else:
        print "length of unknown {}".format(line_length)


def train_matcher_example():
    matcher = Spacy_Matcher(nlp.vocab)
    matcher.add(entity_key='1', label='FOOD', attrs={},
                specs=[[{spacy.attrs.LOWER: 'curly'}, {spacy.attrs.LOWER: 'fries'}]], on_match=merge_phrases)
    matcher.add(entity_key='2', label='FOOD', attrs={}, specs=[[{spacy.attrs.LOWER: 'pizza'}]], on_match=merge_phrases)
    matcher.add(entity_key='3', label='FOOD', attrs={},
                specs=[[{spacy.attrs.LOWER: 'cheese'}, {spacy.attrs.LOWER: 'burger'}]], on_match=merge_phrases)
    matcher.add_pattern(
        '4',
        [
            {
                spacy.attrs.LOWER: "potatoes"
            },

            {spacy.attrs.IS_PUNCT: True},

        ],
        label='FOOD'
    )
    doc = nlp(u'cheese burger and  pizza  eggnog tofu yogurt banana apple banana, apple!')
    matcher(doc)


def train_matcher():
    matcher = Spacy_Matcher(nlp.vocab)
    for directory, dir_names, file_names in os.walk(data_path):
        for file_name in file_names:
            file_name = os.path.join(directory, file_name)

            with open(file_name, 'r') as f:
                if not file_name.endswith("txt"):
                    continue
                for i in f.readlines():
                    i = i.decode("utf-8")
                    i = i.lower().strip().replace('\n', '').replace(r"\(.*\)", "")

                    create_matcher(matcher, i)
        break
    return matcher


def extract_mention_reviews(matcher):
    mention_file = os.path.join(data_path, "mention.txt")
    reviews_file = os.path.join(data_path, "reviews100000.json")
    with open(mention_file, "w") as mention:
        with open(reviews_file) as reviews:
            for index, review in enumerate(reviews.readlines()):
                logger.info("Review of Customer is {}".format(review))
                review = json.loads(review)
                review_text = review['text'].encode('utf-8').strip().decode('utf-8').replace('\n', ' ')
                mention_text = get_food_mentions(matcher, review_text)
                logger.info("Mention is {}".format(mention_text))
                if mention_text != "":
                    mention.write(
                        review["business_id"] + "~" + review[
                            "review_id"] + "~" + review_text + "~" + mention_text + "~" + str(review["stars"]))
                    mention.write("\n")


if __name__ == "__main__":
    logger = logging.getLogger("Train_Matcher")
    file_handler = logging.FileHandler("logs/train_matcher.log", mode="w")
    logger.addHandler(file_handler)
    args = parse_args()
    if args.log_level == "INFO":
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.DEBUG)
    try:
        logger.info("Start train matcher")
        food_matcher = train_matcher()
        logger.info("Completed train matcher")
        logger.info("Start mention extraction")
        extract_mention_reviews(food_matcher)
        logger.info("Completed mention extraction")
    except Exception as exp:
        logger.error("Train matcher failed because of {}".format(exp))
