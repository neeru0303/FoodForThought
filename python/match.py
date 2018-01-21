from meta import Restaurant, Mention
import re

reload


class Match:
    def __init__(self):
        self.possibleMatches = {}
        self.allReviews = {}
        self.pattern = re.compile(r'[,\s\.-]+')

    def matcher(self, mentions):
        x = []
        for i in mentions:
            if mentions[i].text != "":
                self.match_run(mentions[i])

    def match_run(self, mention):
        raise Exception("match_run is not implemented")


class ExactMatcher(Match):
    def match_run(self, mention):
        for i in mention.restaurant.items:
            if i == mention.mention.strip():
                mention.add_item(i)


class FuzzyMatcher(Match):
    def edit_distance(self, str1, str2, m, n):
        d = [[0 for i in range(n + 1)] for j in range(m + 1)]
        # print m,n
        # print d
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
        for i in mention.restaurant.items:
            # print i,mention.mention.strip(),len(i)*2 , 	len(mention.mention.strip())
            if abs(len(i) - len(mention.mention.strip())) > 4:
                # print "yes"
                continue
            elif self.edit_distance(i, mention.mention.strip(), len(i), len(mention.mention.strip())) < 4:
                mention.add_item(i)
            # print self.editDistance(i,mention.mention.strip(),len(i),len(mention.mention.strip()))


class PartialMatcher(Match):
    def match_run(self, mention):
        # print "yes"
        for i in mention.restaurant.items:
            cnt = 0
            matched = []
            for j in self.pattern.split(mention.mention.strip()):
                if j in i and j not in matched and j != "":
                    cnt += 1
                    matched.append(j)
            if cnt > len(self.pattern.split(i)) / 2:
                # print i,mention.reviewid,cnt,mention.mention,matched,self.pattern.split(mention.mention.strip())
                mention.add_item(i)


class SubStringMatcher(Match):
    def match_run(self, mention):
        for i in mention.restaurant.items:
            x = self.pattern.split(mention.mention.strip())
            for j in range(0, len(x), 2):
                try:
                    x = re.search(" ".join(x[j:j + 2]), i).group()
                    mention.add_item(i)
                    break
                except:
                    pass


class SVMMatcher(Match):
    pass
