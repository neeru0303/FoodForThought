from Meta import Restaurant,Mention
import re
reload


class Match:
	def __init__(self):
		self.possibleMatches={}
		self.allReviews={}
		self.pattern = re.compile(r"\s|,|\.|;|-|\(|\)")
	def matcher(self,mentions):
		x=[]
		for i in mentions:
			self.doMatch(mentions[i])
	def doMatch(self,mention):
		pass

class ExactMatcher(Match):
	def doMatch(self,mention):
		for i in mention.restaurant.items:
			if i == mention.mention.strip():
				mention.addItem(i)

class FuzzyMatcher(Match):
	def doMatch(self,mention):
		pass

class PartialMatcher(Match):
	def doMatch(self,mention):
		#print "yes"
		
		for i in mention.restaurant.items:
			cnt = 0
			
			for j in self.pattern.split(mention.mention.strip()):
				if j in i:
					cnt+=1
			if cnt > len(self.pattern.split(i))/2:
				print i,mention.reviewid
				mention.addItem(i)

		


class SVMMatcher(Match):
	def doMatch(self,mention):
		pass


