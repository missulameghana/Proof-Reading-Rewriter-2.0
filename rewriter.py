from nltk.corpus import wordnet
from iitb_dict import iitb_dict
def syno(word):
	word=word.lower()
	if word in iitb_dict.keys():
		return {iitb_dict[word]}
	else:
		synonyms = []
		#ib = wordnet.synset(wordnet.synsets(word)[0].name())
		#print(ib)
		for syn in wordnet.synsets(word):
			#print(syn)
			for l in syn.lemmas():
				synonyms.append(l.name())
				# if word != l.name():
				# 	cb = wordnet.synset(wordnet.synsets(l.name())[0].name())
				# 	print(l.name()+" "+str(ib.wup_similarity(cb)))	

						

		return set(synonyms)
# print(syno("active"))
	