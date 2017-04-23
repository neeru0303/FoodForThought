from __future__ import unicode_literals
import spacy
import re
import os
import json

nlp = spacy.load('en')

def merge_phrases(matcher, doc, i, matches):
    '''
    Merge a phrase. We have to be careful here because we'll change the token indices.
    To avoid problems, merge all the phrases once we're called on the last match.
    '''
    if i != len(matches)-1:
        return None
    spans = [(ent_id, label, doc[start : end]) for ent_id, label, start, end in matches]
    for ent_id, label, span in spans:
        span.merge('NNP' if label else span.root.tag_, span.text, nlp.vocab.strings[label])


def extractMentionReviews(text):
	x=text.lower()
	x=nlp(x)
	try:
		matcher(x)
	except:
		pass
	s=""
	for ent in x:
		if ent.ent_type_=='FOOD':
			#print ent,type(ent.string)
			#print dir(ent)
			s+=ent.text+" "
	print "mention is {}".format(s)
	return s

  			


cnt=5
def createMatcher(x):
	global cnt
	x=re.split(r'[,|\s]*',i)
	if len(x)==1:
		#print x
		matcher.add(entity_key=str(cnt), label='FOOD', attrs={}, specs=[[{spacy.attrs.LOWER: x[0]}]], on_match=merge_phrases)
		cnt+=1
	elif len(x)==2:
		cnt+=1
		matcher.add(entity_key=str(cnt), label='FOOD', attrs={}, specs=[[{spacy.attrs.LOWER: x[0]}, {spacy.attrs.LOWER: x[1]}]], on_match=merge_phrases)
	elif len(x)==3:
		cnt+=1
		#print x
		matcher.add(entity_key=str(cnt), label='FOOD', attrs={}, specs=[[{spacy.attrs.LOWER: x[0]}, {spacy.attrs.LOWER: x[1]}, {spacy.attrs.LOWER: x[2]}]], on_match=merge_phrases)
	elif len(x)==4:
		cnt+=1
		#print x
		matcher.add(entity_key=str(cnt), label='FOOD', attrs={}, specs=[[{spacy.attrs.LOWER: x[0]}, {spacy.attrs.LOWER: x[1]}, {spacy.attrs.LOWER: x[2]}, {spacy.attrs.LOWER: x[3]}]], on_match=merge_phrases)
	elif len(x)==5:
		cnt+=1
		#print x
		matcher.add(entity_key=str(cnt), label='FOOD', attrs={}, specs=[[{spacy.attrs.LOWER: x[0]}, {spacy.attrs.LOWER: x[1]}, {spacy.attrs.LOWER: x[2]}, {spacy.attrs.LOWER: x[3]},{spacy.attrs.LOWER: x[4]}]], on_match=merge_phrases)
	elif len(x)==6:
		cnt+=1
		#print x
		matcher.add(entity_key=str(cnt), label='FOOD', attrs={}, specs=[[{spacy.attrs.LOWER: x[0]}, {spacy.attrs.LOWER: x[1]}, {spacy.attrs.LOWER: x[2]}, {spacy.attrs.LOWER: x[3]},{spacy.attrs.LOWER: x[4]},{spacy.attrs.LOWER: x[5]}]], on_match=merge_phrases)
	elif len(x)==7:
		cnt+=1
		#print x
		matcher.add(entity_key=str(cnt), label='FOOD', attrs={}, specs=[[{spacy.attrs.LOWER: x[0]}, {spacy.attrs.LOWER: x[1]}, {spacy.attrs.LOWER: x[2]}, {spacy.attrs.LOWER: x[3]},\
			{spacy.attrs.LOWER: x[4]},{spacy.attrs.LOWER: x[5]},{spacy.attrs.LOWER: x[6]}]], on_match=merge_phrases)
	elif len(x)==8:
		cnt+=1
		#print x
		matcher.add(entity_key=str(cnt), label='FOOD', attrs={}, specs=[[{spacy.attrs.LOWER: x[0]}, {spacy.attrs.LOWER: x[1]}, {spacy.attrs.LOWER: x[2]}, {spacy.attrs.LOWER: x[3]},\
						{spacy.attrs.LOWER: x[4]},{spacy.attrs.LOWER: x[5]},{spacy.attrs.LOWER: x[6]},{spacy.attrs.LOWER: x[7]}]], on_match=merge_phrases)
	elif len(x)==9:
		cnt+=1
		#print x
		matcher.add(entity_key=str(cnt), label='FOOD', attrs={}, specs=[[{spacy.attrs.LOWER: x[0]}, {spacy.attrs.LOWER: x[1]}, {spacy.attrs.LOWER: x[2]}, {spacy.attrs.LOWER: x[3]},\
						{spacy.attrs.LOWER: x[4]},{spacy.attrs.LOWER: x[5]},{spacy.attrs.LOWER: x[6]},{spacy.attrs.LOWER: x[7]},{spacy.attrs.LOWER: x[8]}]], on_match=merge_phrases)
	elif len(x)>=10:
		cnt+=1
		#print x
		matcher.add(entity_key=str(cnt), label='FOOD', attrs={}, specs=[[{spacy.attrs.LOWER: x[0]}, {spacy.attrs.LOWER: x[1]}, {spacy.attrs.LOWER: x[2]}, {spacy.attrs.LOWER: x[3]},\
						{spacy.attrs.LOWER: x[4]},{spacy.attrs.LOWER: x[5]},{spacy.attrs.LOWER: x[6]},{spacy.attrs.LOWER: x[7]},{spacy.attrs.LOWER: x[8]}]], on_match=merge_phrases)
	else:
		print "length of unknown {}".format(len(x))	



matcher = spacy.matcher.Matcher(nlp.vocab)
matcher.add(entity_key='1', label='FOOD', attrs={}, specs=[[{spacy.attrs.LOWER: 'curly'}, {spacy.attrs.LOWER: 'fries'}]], on_match=merge_phrases)
matcher.add(entity_key='2', label='FOOD', attrs={}, specs=[[{spacy.attrs.LOWER: 'pizza'}]], on_match=merge_phrases)
matcher.add(entity_key='3', label='FOOD', attrs={}, specs=[[{spacy.attrs.LOWER: 'cheese'}, {spacy.attrs.LOWER: 'burger'}]], on_match=merge_phrases)
matcher.add_pattern(
    '4',
    [ 
        { 
          spacy.attrs.LOWER: "potatoes"
        },
        
        
        {spacy.attrs.IS_PUNCT: True},
        
    ],
    label='FOOD' 
)
doc = nlp(u'cheese burger and  pizza  eggnog tofu yogurt banana apple')
matcher(doc)


p = os.getcwd()
p = os.path.join(p,"data")
os.chdir(p)
for i,j,k in os.walk(p):
	for file in k:
		#datafile = os.path.join(i,file)
		print file
		with open(file,'r') as f:
			for i in f.readlines():
				i=i.decode("utf-8")
				i=i.lower().strip().replace('\n','').replace(r"\(.*\)","")

				createMatcher(i)
				



print cnt


"""
with open('FOOD_DES.txt','r') as f:
	with open('dishes.txt','w') as w:
		for i in f.readlines():
			x = i.split('~^~')
			w.write(x[2])
			w.write("")
"""																																				

matcher(doc)

for ent in doc:
  print(ent,ent.ent_type_)


with open("mention.txt","w") as mention: 
	with open("reviews100.json") as reviews:
		for cnt,i in enumerate(reviews.readlines()):
			x=json.loads(i)
			x=x['text'].strip().replace('\n',' ')
			mentiontext=extractMentionReviews(x)
			if mentiontext!="":
				mention.write(x+"~"+mentiontext)
				mention.write("\n")
			if cnt==80:
				break