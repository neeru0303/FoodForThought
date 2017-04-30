from Meta import Restaurant,Mention
import re
reload

class Match:
	def __init__(self):
		self.possibleMatches={}
		self.allReviews={}
		self.pattern = re.compile(r'[,\s\.-]+')
	def matcher(self,mentions):
		x=[]
		for i in mentions:
			if mentions[i].text!="":
				self.doMatch(mentions[i])
	def doMatch(self,mention):
		pass

class ExactMatcher(Match):
	def doMatch(self,mention):
		for i in mention.restaurant.items:
			if i == mention.mention.strip():
				mention.addItem(i)

class FuzzyMatcher(Match):
	def editDistance(self,str1,str2,m,n):
		if len(str1)==0:
			return len(str2)
		if len(str2)==0:
			return len(str1)
		if str1[m-1]==str2[n-1]:
			return self.editDistance(str1[:m-1],str2[:n-1],m-1,n-1)
		else: 
			return 1+ min(self.editDistance(str1[:m],str2[:n-1],m,n-1),
						self.editDistance(str1[:m-1],str2[:n-1],m-1,n-1),
						self.editDistance(str1[:m-1],str2[:n],m-1,n),
						)
	
	def doMatch(self,mention):
		for i in mention.restaurant.items:
			print i,mention.mention.strip(),len(i)*2 , 	len(mention.mention.strip())
			if len(i)*2 <len(mention.mention.strip()):
				print "yes"
				continue
			elif self.editDistance(i,mention.mention.strip(),len(i),len(mention.mention.strip())) <4:
				mention.addItem(i)
			print self.editDistance(i,mention.mention.strip(),len(i),len(mention.mention.strip()))

class PartialMatcher(Match):
	def doMatch(self,mention):
		#print "yes"
		for i in mention.restaurant.items:
			cnt = 0
			matched = []
			for j in self.pattern.split(mention.mention.strip()):
				if j in i and j not in matched and j!="":
					cnt+=1
					matched.append(j)
			if cnt > len(self.pattern.split(i))/2:
				#print i,mention.reviewid,cnt,mention.mention,matched,self.pattern.split(mention.mention.strip())
				mention.addItem(i)

		
class SubStringMatcher(Match):
	def doMatch(self,mention):
		for i in mention.restaurant.items:
			x = self.pattern.split(mention.mention.strip())
			for j in range(0,len(x),2):
				try:
					x = re.search(" ".join(x[j:j+2]),i).group()
					mention.addItem(i)
					break
				except:
					pass




class SVMMatcher(Match):
	def doMatch(self,mention):
		pass


