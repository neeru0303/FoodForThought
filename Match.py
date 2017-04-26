restaurantItems={'3EjjtHEFdTZST55js1A18A':['sweet potato']}


class Match:
	def matcher(self,mentions):
		for i in mentions:	
			self.doMatch(i)
	def doMatch(self,mention):
		pass

class ExactMatcher(Match):
	def doMatch(self,mention):
		possibleMatches={}
		mention=mention.split('~')
		for i in restaurantItems.get(mention[0],[]):
			x=mention[3].strip()
			if x==i:
				
				possibleMatches[mention[1]]=i
		
		return possibleMatches


class FuzzyMatcher(Match):
	def doMatch(self,mention):
		pass

class PartialMatcher(Match):
	def doMatch(self,mention):
		pass


class SVMMatcher(Match):
	def doMatch(self,mention):
		pass


