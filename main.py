from rewriter import syno
import re
import nltk
string = input("Enter some text: ")
no_specials_string = re.sub('[!#?,:";]', '', string)
sentences = no_specials_string.split('.')
words = []
tags = ['NN','NNS','JJ','JJR','JJS','FW','RB','RBR','RBS']
tags_v = ['VB','VBD','VBG','VBN','VBP','VBZ']
helping_verbs=['am', 'is', 'are', 'was', 'were', 'be', 'being','been',
			'will', 'would', 'shall', 'should', 'may', 'might', 'must', 'can','could',
			'do', 'does','did','have','having','has','had']
for sentence in sentences:
    for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
    	word_lower = word.lower()
    	if pos in tags:
        	words.append(word)
    	elif pos in tags_v:
    		if word_lower not in helping_verbs:
    			words.append(word)

for word in list(dict.fromkeys(words)):
	syno_list = syno(word)	
	if syno_list:
		print("Suggested list of synonyms for "+word+" "+str(syno_list)) 