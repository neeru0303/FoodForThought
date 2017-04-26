class Restaurant:
	def __init__(self,restaurantid,name,city,rating,items=['fries']):
		self.restaurantid=restaurantid
		self.name=name
		self.rating = rating
		self.city = city
		self.items= items


class Mention:
	def __init__(self,restaurant,reviewid,text,mention,sentiment):
		#print type(restaurant)
		self.restaurant = restaurant
		self.reviewid = reviewid
		self.text = text
		self.mention = mention
		self.sentiment = sentiment
		self.items=[]
	def addItem(self,item):
		self.items.append(item)