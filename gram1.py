import nltk
import urllib
import requests
from pattern.en import tag,suggest,ngrams,parse,parsetree,pprint,lexeme,referenced
def joinlist(l):
	return '/'.join(l)
WHfam=["what","when","where","who","whom","which","whose","why","how"]
Demons=["this","that","these","those"]
Aux=['be', 'am', 'are', 'is', 'being', 'was', 'were', 'been',"'s"] #, "aren't", "isn't", "wasn't", "weren't"]
Verbs=["VBZ","VB","VBP","VBD","VBN","VBG"]
Perfect=["has","have","had"]
Future=["will","shall","should","would"]
Possessives=[["i","my","me","mine"],["she","her","hers"],["he","him","his"],["you","your","yours"],["it","it's"],["we","us","our","ours"],["they","them","their","theirs"]]
Poss=["i","my","me","mine","she","her","hers","he","him","his","you","your","yours","it","it's","we","us","our","ours","they","them","their","theirs"]
Articles=["a","an","the"]
Prepositions=["in","on","at"]

instr=input()
var=instr.lower()
# token=nltk.word_tokenize(var)
trigrams=ngrams(var,3)

def query(v,i):
	encoded_query = urllib.parse.quote(v)
	params = {'corpus': 'eng-us', 'query': encoded_query, 'topk': 10, 'format': 'tsv'}
	params = '&'.join('{}={}'.format(name, value) for name, value in params.items())

	response = requests.get('https://api.phrasefinder.io/search?' + params)

	assert response.status_code == 200

	s=response.text
	d={}
	x=s.split("\n")
	x.pop()
	# #print(x)
	for y in x:
		z=y.split("\t")
		val=z[0].lower()
		l=[]
		lis=val.split(" ")
		# lis = lis[1:2]
		for word in lis:
			l=l+[word.split("_")[0]]
		val=" ".join(l)
		if val in d:
			d[val]+=float(z[i])
		else:
			d[val]=float(z[i])

	return d

def processArt(t):
	# lis=nltk.pos_tag(nltk.word_tokenize(s))
	# lis=x.split(" ")
	l=[]
	cnt=0
	for ele in t:
		cnt=cnt+1
		# y=ele[1]
		# word=ele[0]
		if ele=="a":
			if referenced(t[count]=="a"):
				l=l+[joinlist(["a","the"])]
			else:
				l=l+[joinlist(["an","the"])]
		elif ele=="an":
			if referenced(t[count]=="an"):
				l=l+[joinlist(["an","the"])]
			else:
				l=l+[joinlist(["a","the"])]
		else:
			l=l+[ele]
	return " ".join(l)


def process(s):
	# x=parse(s,tokenize=True,tags=True,chunks=True,encoding='utf-8')
	# lis=x.split(" ")
	lis=nltk.pos_tag(nltk.word_tokenize(s))
	l=[]
	# print(lis)
	for ele in lis:
		y=ele[1]
		word=ele[0]
		# if word in WHfam:
		# 	l=l+[joinlist(WHfam)]
		# if word in Demons:
		# 	l=l+[joinlist(Demons)]
		# if word.lower() in Poss:
		# 	for xyz in Possessives:
		# 		if word.lower() in xyz:
		# 			l=l+[joinlist(xyz)]
		# 			break
		if y in Verbs:
			# print(word)
			if word in Aux:
				l=l+[joinlist(Aux)]
			else:
				# print("Hi")
				l=l+[joinlist(lexeme(word))]
		else:
			l=l+[word]
	return " ".join(l)

def processWH(s):
	lis=s.split(" ")
	# lis=x.split(" ")
	l=[]
	for ele in lis:
		# y=ele[1]
		# word=ele
		if ele in WHfam:
			l=l+[joinlist(WHfam)]
		# elif y in Verbs:
		# 	if word in Aux:
		# 		l=l+[joinlist(Aux)]
		# 	else:
		# 		l=l+[joinlist(lexeme(word))]
		else:
			l=l+[ele]
	return " ".join(l)

def processDem(t):
	# lis=nltk.pos_tag(nltk.word_tokenize(s))
	# lis=x.split(" ")
	l=[]
	for ele in t:
		# y=ele[1]
		# word=ele[0]
		if ele in Demons:
			l=l+[joinlist(Demons)]
		# elif y in Verbs:
		# 	if word in Aux:
		# 		l=l+[joinlist(Aux)]
		# 	else:
		# 		l=l+[joinlist(lexeme(word))]
		else:
			l=l+[ele]
	return " ".join(l)

def processPoss(t):
	# lis=nltk.pos_tag(nltk.word_tokenize(s))
	# lis=x.split(" ")
	l=[]
	# cnt=0
	for ele in t:
		# cnt=cnt+1
		# y=ele[1]
		# word=ele[0]
		if ele in Poss:
			for xyz in Possessives:
				if ele in xyz:
					l=l+[joinlist(xyz)]
					break
		else:
			l=l+[word]
	return " ".join(l)

def processPrep(t):
	# lis=nltk.pos_tag(nltk.word_tokenize(s))
	# lis=x.split(" ")
	l=[]
	for ele in t:
		# y=ele[1]
		# word=ele[0]
		if ele in Prepositions:
			l=l+[joinlist(Prepositions)]
		# elif y in Verbs:
		# 	if word in Aux:
		# 		l=l+[joinlist(Aux)]
		# 	else:
		# 		l=l+[joinlist(lexeme(word))]
		else:
			l=l+[ele]
	return " ".join(l)


# print(process("He play cricket"))
threshold=10000;
# threshold_f=;
count = 0;
suggestions=[]
verb_list=[]
# final_suggestions={}


for t in trigrams:
	# count = count + 1
	# if(t[0] in WHfam):
	# 	st=st+" "+trigrams[count][0]
	# print(st)
	if(t[0] in Articles or t[1] in Articles):
		st=" ".join(t)
		s=query(st,1)
		if(len(s)==0):
			suggest=processArt(t)
			# print(suggest)
			final=query(suggest,6)
			suggestions=suggestions+[dict(filter(lambda elem: elem[1]>=0.2, final.items()))]
		elif(threshold>=s[st.lower()]):
			suggest=processArt(t)
			# print(suggest)
			final=query(suggest,6)
			suggestions=suggestions+[dict(filter(lambda elem: elem[1]>=0.2, final.items()))]
			# print(final)
		# else:
		# 	suggestions=suggestions+[{}]
print(suggestions)

for t in trigrams:
	# count = count + 1
	st=" ".join(t)
	# if(t[0] in WHfam):
	# 	st=st+" "+trigrams[count][0]
	# print(st)
	s=query(st,1)
	if(len(s)==0):
		suggest=process(st)
		print(suggest)
		# print(suggest)
		final=query(suggest,6)
		print(final)
		verb_list=verb_list+[dict(filter(lambda elem: elem[1]>=0.2, final.items()))]
		suggestions=suggestions+[dict(filter(lambda elem: elem[1]>=0.2, final.items()))]
	elif(threshold>=s[st.lower()]):
		suggest=process(st)
		# print(suggest)
		final=query(suggest,6)
		print(final)
		verb_list=verb_list+[dict(filter(lambda elem: elem[1]>=0.2, final.items()))]
		suggestions=suggestions+[dict(filter(lambda elem: elem[1]>=0.2, final.items()))]
		# print(final)
	else:
		verb_list=verb_list+[{}]
print(suggestions)
print("here")

for t in trigrams:
	# count = count + 1
	# if(t[0] in WHfam):
	# 	st=st+" "+trigrams[count][0]
	# print(st)
	if(t[0] in Demons or t[1] in Demons or t[2] in Demons):
		st=" ".join(t)
		s=query(st,1)
		if(len(s)==0):
			suggest=processDem(t)
			# print(suggest)
			final=query(suggest,6)
			suggestions=suggestions+[dict(filter(lambda elem: elem[1]>=0.2, final.items()))]
		elif(threshold>=s[st.lower()]):
			suggest=processDem(t)
			# print(suggest)
			final=query(suggest,6)
			suggestions=suggestions+[dict(filter(lambda elem: elem[1]>=0.2, final.items()))]
			# print(final)
		# else:
		# 	suggestions=suggestions+[{}]
print(suggestions)

for t in trigrams:
	count=count+1
	if(t[0] in WHfam):
		st=" ".join(t)
		if not verb_list[count]:
			st=st+" "+trigrams[count][2]
		else:
			st=t[0]+" "+list(verb_list[count].keys())[0]
			# print(st)
		s=query(st,1)
		if(len(s)==0):
			suggest=processWH(st)
			final=query(suggest,6)
			suggestions=suggestions+[dict(filter(lambda elem: elem[1]>=0.2, final.items()))]
		elif(threshold>=s[st.lower()]):
			suggest=processWH(st)
			# print(suggest)
			final=query(suggest,6)
			suggestions=suggestions+[dict(filter(lambda elem: elem[1]>=0.2, final.items()))]
		# else:
		# 	final=s
print(suggestions)
for t in trigrams:
	# count = count + 1
	# if(t[0] in WHfam):
	# 	st=st+" "+trigrams[count][0]
	# print(st)
	if(t[0] in Possessives or t[1] in Possessives or t[2] in Possessives):
		st=" ".join(t)
		s=query(st,1)
		if(len(s)==0):
			suggest=processPoss(t)
			print(suggest)
			final=query(suggest,6)
			suggestions=suggestions+[dict(filter(lambda elem: elem[1]>=0.2, final.items()))]
		elif(threshold>=s[st.lower()]):
			suggest=processPoss(t)
			print(suggest)
			final=query(suggest,6)
			suggestions=suggestions+[dict(filter(lambda elem: elem[1]>=0.2, final.items()))]
			# print(final)
		# else:
		# 	suggestions=suggestions+[{}]
print(suggestions)

for t in trigrams:
	# count = count + 1
	# if(t[0] in WHfam):
	# 	st=st+" "+trigrams[count][0]
	# print(st)
	if(t[0] in Prepositions or t[1] in Prepositions or t[2] in Prepositions):
		st=" ".join(t)
		s=query(st,1)
		if(len(s)==0):
			suggest=processPrep(t)
			print(suggest)
			final=query(suggest,6)
			suggestions=suggestions+[dict(filter(lambda elem: elem[1]>=0.2, final.items()))]
		elif(threshold>=s[st.lower()]):
			suggest=processPrep(t)
			print(suggest)
			final=query(suggest,6)
			suggestions=suggestions+[dict(filter(lambda elem: elem[1]>=0.2, final.items()))]
			# print(final)
		# else:
		# 	suggestions=suggestions+[{}]
print(suggestions)

# count=0
# for t in trigrams:
# 	count=count+1
# 	if(t[0] in WHfam):
# 		st=" ".join(t)
# 		if not suggestions[count]:
# 			st=st+" "+trigrams[count][2]+" "+trigrams[count+1][0]
# 		else:
# 			r=list(suggestions[count].keys())[0].split(" ")[0]
# 			st=t[0]+" "+list(suggestions[count].keys())[0]+" "+r
# 			# print(st)
# 		s=query(st,1)
# 		if(len(s)==0):
# 			suggest=processWH(st)
# 			final=query(suggest,6)
# 			final=dict(filter(lambda elem: elem[1]>=0.2, final.items()))
# 		elif(threshold>=s[st.lower()]):
# 			suggest=processWH(st)
# 			# print(suggest)
# 			final=query(suggest,6)
# 			final=dict(filter(lambda elem: elem[1]>=0.2, final.items()))
# 		else:
# 			final=s
# 		print(final)



