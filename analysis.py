import Match

exactmatch = Match.ExactMatcher()
with open("data/mention.txt") as mention:
	x=exactmatch.matcher(mention.readlines())
	
	if x is not None:
		print x
	