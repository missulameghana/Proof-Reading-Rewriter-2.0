from nltk.corpus import wordnet
def syno(word):
	synonyms = []
	for syn in wordnet.synsets(word):
		for l in syn.lemmas():
			synonyms.append(l.name())			

	return set(synonyms)
	