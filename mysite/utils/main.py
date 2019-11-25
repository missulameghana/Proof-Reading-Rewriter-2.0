from .rewriter import syno
import re
import nltk
def main(sentence):
	dickt2 = {}
	string = sentence
	no_specials_string = re.sub('[#,:";]', '', string)
	sentences=re.split('\? |\?|\. |\.|! |!',no_specials_string)
	sentences.pop();
	#print(sentences)
	left = {}
	right = {}
	words = []
	tags = ['NN','NNS','JJ','JJR','JJS','FW','RB','RBR','RBS']
	tags_v = ['VB','VBD','VBG','VBN','VBP','VBZ']
	helping_verbs=['am', 'is', 'are', 'was', 'were', 'be', 'being','been',
				'will', 'would', 'shall', 'should', 'may', 'might', 'must', 'can','could',
				'do', 'does','did','have','having','has','had']
	for sentence in sentences:
		word_list = sentence.split()
		n = len(word_list)
		i = 0
		#print(word_list)
		for word in word_list:
			if i == 0:
				left[word] = ""
				right[word] = word_list[i+1]
				i = i + 1
			elif i == n-1:
				left[word] = word_list[i-1]
				right[word] = ""
				i = i + 1
			else:
				left[word] = word_list[i-1]
				right[word] = word_list[i+1]
				i = i + 1
			
		for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
			word_lower = word.lower()
			if pos in tags:
				words.append(word)
			elif pos in tags_v:
				if word_lower not in helping_verbs:
					words.append(word)

	print(words)
	# print(left)
	# print(right)
	for word in list(dict.fromkeys(words)):
		# print(word)
		# print(left[word])
		# print(right[word])
		syno_list = syno(left[word],word,right[word])
		# print("recieved")
		# print(syno_list)
		if syno_list:
			dickt2[word]=syno_list
	return dickt2