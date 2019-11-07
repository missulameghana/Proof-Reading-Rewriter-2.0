from nltk.corpus import wordnet
def syno(word):
	synonyms = []
	antonyms = []
	for syn in wordnet.synsets(word):
		for l in syn.lemmas():
			synonyms.append(l.name())
			if l.antonyms():
				 antonyms.append(l.antonyms()[0].name())


	return set(synonyms)
	