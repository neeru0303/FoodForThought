import Restaurant

print Restaurant.items
class Match:
	def __init__(self):
		self.possibleMatches={}
		self.allReviews={}
	def matcher(self,mentions):
		x=[]
		for i in mentions:
			if self.doMatch(i) is not None:	
				self.doMatch(i)
		return self.allReviews

			#return self.doMatch(i)
	def doMatch(self,mention):
		pass

class ExactMatcher(Match):
	def doMatch(self,mention):
		#possibleMatches={}
		mention=mention.split('~')
		#print mention
		for i in Restaurant.items.get(mention[0],[]):
			#print "i "+i
			#print restaurantItems.get(mention[0],[])
			x=mention[3].strip()
			#print "x "+x
			if x==i:
				print "mention "+mention[1],i
				self.possibleMatches[mention[1]]=i
				self.allReviews[mention[0]]=self.possibleMatches[mention[1]]
		if len(self.possibleMatches)!=0:
			#print self.possibleMatches
			return self.possibleMatches


class FuzzyMatcher(Match):
	def doMatch(self,mention):
		pass

class PartialMatcher(Match):
	def doMatch(self,mention):
		pass


class SVMMatcher(Match):
	def doMatch(self,mention):
		pass


