from nltk.corpus import wordnet
from iitb_dict import iitb_dict
import urllib
import requests
import csv
import sqlite3
def syno(left,word,right):
	word=word.lower()
	if word in iitb_dict.keys():
		return {iitb_dict[word]}
	else:
		synonyms = []
		for syn in wordnet.synsets(word):
			for l in syn.lemmas():
				synonyms.append(l.name())						
		syn_freq_dict = {}
		S = set(synonyms)
		S.discard(word)
		#print(S)
		syn_str = ""
		if len(S) == 0:
			return []
		for syn in S:
			syn_str = syn_str +"/"+ syn
		syn_str = syn_str[1:]
		print(syn_str)
		encoded_query = urllib.parse.quote(left+" "+syn_str+" "+right)
		params = {'corpus': 'eng-us', 'query': encoded_query, 'topk': 10, 'format': 'tsv'}
		params = '&'.join('{}={}'.format(name, value) for name, value in params.items())

		response = requests.get('https://api.phrasefinder.io/search?' + params)

		assert response.status_code == 200
		s = response.text
		d={}
		x=s.split("\n")
		x.pop()
		# #print(x)
		for y in x:
			z=y.split("\t")
			val=z[0].lower()
			l=[]
			lis=val.split(" ")
			lis = lis[1:2]
			for word in lis:
				l=l+[word.split("_")[0]]
			val=" ".join(l)
			if val in d:
				d[val]+=float(z[6])
			else:
				d[val]=float(z[6])

		print(d)
		# 	with open("out.tsv") as fin:
		# 	    line = fin.readline()
		# 	    match_count = sum(int(r[1]) for r in csv.reader(line,delimiter='\t'))

			
		# 	syn_freq_dict[syn] = match_count


		# sorted(syn_freq_dict.items(), key=operator.itemgetter(1))
		Sf = []
		n = len(d)
		if n == 0:
			##print(Sf)
			#print("sent0")
			return Sf
		elif n == 1:
			#print(d)
			Sf.append(list(d.keys())[0])
			#print("sent1")
			return Sf
		elif n == 2:
			Sf.append(list(d.keys())[0])
			Sf.append(list(d.keys())[1])
			#print("sent2")
			return Sf
		else:
			#print("sent>3")
			Sf.append(list(d.keys())[0])
			Sf.append(list(d.keys())[1])
			Sf.append(list(d.keys())[2])
			return Sf
#syno("i","look","good")