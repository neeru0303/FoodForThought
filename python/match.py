#!/usr/bin/env python
"""
Module for various Match patterns

"""

import re

class Match(object):
    """
    base class for all matches
    """
    def __init__(self):
        self._pattern = re.compile(r'[,\s\.-]+')

    def matcher(self, mentions):
        """
        perform match on all mentions
        :param mentions:
        :return:
        """
        for i in mentions:
               if mentions[i].mention_text != "":
                  self.match_run(mentions[i])


    def match_run(self, mention):
        """
        abstract method for match run
        :param mention:
        :return:
        """
        raise Exception("match_run is not implemented")


class ExactMatcher(Match):
    """
    Class for Exact match
    """
    def match_run(self, mention):   
        """
        perform exact match
        :param mention:
        :return:

        Example:

        match is successful
        >>> mention_text = " fries";  items = "fries"

        match is not successful
        >>> mention_text = "curly fries";  items = "fries"
        """
        for i in mention.restaurant.items:
            if i == mention.mention_text.strip():
                mention.add_item(i)


class FuzzyMatcher(Match):
    """
    Match to ignore typos
    """
    @staticmethod
    def edit_distance(str1, str2, m, n):
        """
        Calculate edit distance between 2 strings
        :param str1:
        :param str2:
        :param m: length of string str1
        :param n: length of string str2
        :return:

        Example: edit_distance = 4
        >>> str1 = apple ;str2 = pineapple
        pineapple
        ____apple
        Example: edit_distance = 3
        >>> str1 = approximate str2= appropriate
        approximate
            |||
        appropriate
        """
        d = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m + 1):
            d[i][0] = i
        for j in range(n + 1):
            d[0][j] = j

        for i in range(m + 1):
            for j in range(n + 1):
                # print d[i][j],i,j
                if str1[i - 1] == str2[j - 1]:
                    d[i][j] = d[i - 1][j - 1]
                else:
                    d[i][j] = 1 + min(d[i][j - 1], d[i - 1][j - 1], d[i - 1][j])
        return d[m][n]

    def match_run(self, mention):
        """
        perform fuzzy match
        :param mention:
        :return:

        Example: match is successful
        >>> mention_text = apple ;menu_item = pineapple
        edit_distance = 4

        Example: match is successful
        >>> str1 = approximate str2= appropriate
        edit_distance =  3

        """
        try:
            if not mention.mention_text.strip():
                return
            for i in mention.restaurant.items:
                # print i,mention.mention_text.strip(),len(i)*2 , 	len(mention.mention_text.strip())
                if abs(len(i) - len(mention.mention_text.strip())) > 5:
                    # print "yes"
                    continue
                elif self.edit_distance(i, mention.mention_text.strip(), len(i), len(mention.mention_text.strip())) <= 5:
                    mention.add_item(i)
                # print self.editDistance(i,mention.mention_text.strip(),len(i),len(mention.mention_text.strip()))
        except Exception as err:
                print err
                print len(mention.mention_text)
                print mention.items


class PartialMatcher(Match):
    """
    Partial Match between Restaurant Menu Item and Mention text
    """
    def match_run(self, mention):
        """
        perform partial match
        :param mention:
        :return:

        Example: match is successful
        >>> mention_text = egg pork rolls  ; menu_item = pork rolls

        Example: match is not successful
        >>> mention_text = thai green currry ; menu_item= vegeteble curry

        """
        for i in mention.restaurant.items:
            cnt = 0
            matched = []
            for j in self._pattern.split(mention.mention_text.strip()):
                if j in i and j not in matched and j != "":
                    cnt += 1
                    matched.append(j)
            if cnt > len(self._pattern.split(mention.mention_text.strip())) / 2:
                mention.add_item(i)


class SubStringMatcher(Match):
    """
        Substring Match between Restaurant Menu Item and Mention text
    """
    def match_run(self, mention):
        """
        perform substring match
        :param mention:
        :return:

        Example: match is successful
        >>> mention_text = black beans  ; menu_item = spicy black beans

        Example: match is not successful
        >>> mention_text = green curry ; menu_item= thai curry


        """
        for i in mention.restaurant.items:
            x = self._pattern.split(mention.mention_text.strip())
            for j in range(0, len(x), 2):
                try:
                    x = re.search(" ".join(x[j:j + 2]), i).group()
                    mention.add_item(i)
                    break
                except:
                    pass
