import nltk
import urllib
import requests
from pattern.en import tag,suggest,ngrams,parse,parsetree,pprint,lexeme
def joinlist(l):
	return '/'.join(l)
WHfam=["What","When","Where","Who","Whom","Which","Whose","Why","How"]
Demons=["this","that","these","those"]
Aux=['be', 'am', 'are', 'is', 'being', 'was', 'were', 'been'] #, "aren't", "isn't", "wasn't", "weren't"]
Verbs=["VBZ","VB","VBP","VBD","VBN","VBG"]
Perfect=["has","have","had"]
Future=["will","shall","should","would"]
Possessives=[["i","my","me","mine"],["she","her","hers"],["he","him","his"],["you","your","yours"],["it","its"],["we","us","our","ours"],["they","them","their","theirs"]]
Poss=["i","my","me","mine","she","her","hers","he","him","his","you","your","yours","it","its","we","us","our","ours","they","them","their","theirs"]


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
def process(s):
	x=parse(s,tokenize=True,tags=True,chunks=True,encoding='utf-8')
	lis=x.split(" ")
	l=[]
	print(lis)
	for ele in lis:
		y=ele.split("/")[1]
		word=ele.split("/")[0]
		# if word in WHfam:
		# 	l=l+[joinlist(WHfam)]
		if word in Demons:
			l=l+[joinlist(Demons)]
		elif word.lower() in Poss:
			for xyz in Possessives:
				if word.lower() in xyz:
					l=l+[joinlist(xyz)]
					break
		elif y in Verbs:
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
	x=parse(s,tokenize=True,tags=True,chunks=True,encoding='utf-8')
	lis=x.split(" ")
	l=[]
	for ele in lis:
		y=ele.split("/")[1]
		word=ele.split("/")[0]
		if word in WHfam:
			l=l+[joinlist(WHfam)]
		# elif y in Verbs:
		# 	if word in Aux:
		# 		l=l+[joinlist(Aux)]
		# 	else:
		# 		l=l+[joinlist(lexeme(word))]
		else:
			l=l+[word]
	return " ".join(l)

# print(process("He play cricket"))
threshold=10000;
# threshold_f=;
count = 0;
final_suggestions=[]
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
		final=query(suggest,6)
		final_suggestions=final_suggestions+[dict(filter(lambda elem: elem[1]>=0.09, final.items()))]
	elif(threshold>=s[st.lower()]):
		suggest=process(st)
		print(suggest)
		final=query(suggest,6)
		final_suggestions=final_suggestions+[dict(filter(lambda elem: elem[1]>=0.09, final.items()))]
		# print(final)
	else:
		final_suggestions=final_suggestions+[{}]
print(final_suggestions)

for t in trigrams:
	count=count+1
	if(t[0] in WHfam):
		st=" ".join(t)
		if not final_suggestions[count]:
			st=st+" "+trigrams[count][2]
		else:
			st=t[0]+" "+list(final_suggestions[count].keys())[0]
			# print(st)
		s=query(st,1)
		if(len(s)==0):
			suggest=processWH(st)
			final=query(suggest,6)
			final=dict(filter(lambda elem: elem[1]>=0.09, final.items()))
			print(final)
		elif(threshold>=s[st.lower()]):
			suggest=processWH(st)
			# print(suggest)
			final=query(suggest,6)
			final=dict(filter(lambda elem: elem[1]>=0.09, final.items()))
			print(final)
		else:
			final=s
# count=0
# for t in trigrams:
# 	count=count+1
# 	if(t[0] in WHfam):
# 		st=" ".join(t)
# 		if not final_suggestions[count]:
# 			st=st+" "+trigrams[count][2]+" "+trigrams[count+1][0]
# 		else:
# 			r=list(final_suggestions[count].keys())[0].split(" ")[0]
# 			st=t[0]+" "+list(final_suggestions[count].keys())[0]+" "+r
# 			# print(st)
# 		s=query(st,1)
# 		if(len(s)==0):
# 			suggest=processWH(st)
# 			final=query(suggest,6)
# 			final=dict(filter(lambda elem: elem[1]>=0.09, final.items()))
# 		elif(threshold>=s[st.lower()]):
# 			suggest=processWH(st)
# 			# print(suggest)
# 			final=query(suggest,6)
# 			final=dict(filter(lambda elem: elem[1]>=0.09, final.items()))
# 		else:
# 			final=s
# 		print(final)



