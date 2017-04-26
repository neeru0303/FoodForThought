from Meta import Restaurant,Mention
reload


class Match:
	def __init__(self):
		self.possibleMatches={}
		self.allReviews={}
	def matcher(self,mentions):
		x=[]
		for i in mentions:
			self.doMatch(mentions[i])
	def doMatch(self,mention):
		pass

class ExactMatcher(Match):
	def doMatch(self,mention):
		for i in mention.restaurant.items:
			if i == mention.mention:
				mention.addItem(i)

class FuzzyMatcher(Match):
	def doMatch(self,mention):
		pass

class PartialMatcher(Match):
	def doMatch(self,mention):
		pass


class SVMMatcher(Match):
	def doMatch(self,mention):
		pass


