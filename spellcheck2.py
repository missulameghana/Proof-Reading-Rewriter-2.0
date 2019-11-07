import nltk
import re
with open('words') as word_file:
	english_words=set(word_file.read().split())
var = input("Enter some text: ")
b=0;
i=0;
l=[];
lines=re.split('\? |\?|\. |\.|! |!',var);
for x in lines:
	if(i!=len(lines)-1):
		x1=x.split(" ");
		for w in x1:
			l=[];
			b=0;
			for words in english_words:
				if(nltk.edit_distance(words.lower(),w.lower())==0):
					b=1;
					break;
				elif(nltk.edit_distance(words.lower(),w.lower())==1):
					l.append(words);
			if(b==0):
				print(w,l);
	i=i+1;


