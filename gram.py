import nltk
import urllib
import requests
from pattern.en import tag,suggest,ngrams,parse,parsetree,pprint,lexeme
def joinlist(l):
	return '/'.join(l)
WHfam=["What","When","Where","Who","Whom","Which","Whose","Why","How"]
Demons=["this","that","these","those"]
Aux=['be', 'am', 'are', 'is', 'being', 'was', 'were', 'been', "aren't", "isn't", "wasn't", "weren't"]
Verbs=["VBZ","VB","VBP","VBD","VBN","VBG"]

var=input()
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
def process(s):
	x=parse(s,tokenize=True,tags=True,chunks=True,encoding='utf-8')
	lis=x.split(" ")
	l=[]
	for ele in lis:
		y=ele.split("/")[1]
		word=ele.split("/")[0]
		if word in WHfam:
			l=l+[joinlist(WHfam)]
		elif y in Verbs:
			if word in Aux:
				l=l+[joinlist(Aux)]
			else:
				l=l+[joinlist(lexeme(word))]
		else:
			l=l+[word]
	return " ".join(l)
# print(process("He play cricket"))
threshold=500;
for t in trigrams:
	st=" ".join(t)
	s=query(st,1)
	if(len(s)==0):
		suggest=process(st)
		final=query(suggest,6)
		final=dict(filter(lambda elem: elem[1]>=0.09, final.items()))
	elif(threshold>=s[st.lower()]):
		suggest=process(st)
		print(suggest)
		final=query(suggest,6)
		final=dict(filter(lambda elem: elem[1]>=0.09, final.items()))
	else:
		final=s


