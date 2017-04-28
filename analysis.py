import Match
import json

from Meta import Restaurant,Mention
reload

restaurants={}
mentions={}


def readRestaurant():
	with open("data/restuarants.json") as restaurant :
		for i in restaurant.readlines():
			i=json.loads(i)
			restaurants[i["business_id"]] = Restaurant(i["business_id"],i["name"],i["city"],i["stars"],i.get("items",[]))
			#print i["business_id"],i["name"],i["city"],i["stars"]
			
	#print restuarants

def writeItemMention():
	with open("data/mentionWithItems.txt",'w') as wmention:
		for i in mentions:
			if len(mentions[i].items)!=0:
				mention=mentions[i]
				wmention.write(mention.restaurant.restaurantid+"~"+mention.reviewid+"~"+mention.mention+"~"+mention.sentiment+"~"+"-".join(mention.items)) 
				wmention.write("\n")


def readMentions():
	with open("data/mention.txt") as mention:
		for i in mention.readlines():
			i=i.split("~")
			try:
				#print len(i)
				mentions[i[1]] = Mention(restaurants[i[0]],i[1],i[2],i[3],i[4])
				#print type(mentions[i[1]].restaurant.items)
			except:
				pass





readRestaurant()
readMentions()	
#print type(mentions['apzxETosswLEoNIwHOh7nA'].restaurant)
#exactmatch = Match.ExactMatcher()
#exactmatch.matcher(mentions)
partialmatch = Match.PartialMatcher()
partialmatch.matcher(mentions)
print mentions['VmB6OWKb10tEy8o9EyNzYw'].items
print restaurants['N5dkbfyNWZPxOMWDiJp7TQ'].items
writeItemMention()



"""
exactmatch = Match.ExactMatcher()
with open("data/mention.txt") as mention:
	x=exactmatch.matcher(mention.readlines())
	if x is not None:
		print x
"""	