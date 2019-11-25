# from main import *
from spelling import *
import re
var=input("Enter some text:")
words=re.findall(r"[\w']+|[.!?]",var)
last=len(words)-words[::1].index('.') +1
words=words[:last]
i=-1
for word in words:
	i=i+1
	# print(" ".join(words))
	l=correction(word.lower())
	if len(l)!=0:
		print(" ".join(words))
		print("Suggest list of correct spellings for "+word+" : ",l)
		option=input("Choose any option or to ignore type -1 ")
		if int(option)!=-1:
			if int(option)<len(l):
				# x=dic[word][option+1]
				words[i]=l[int(option)-1]
print(" ".join(words))
i=-1
for word in words:
	i=i+1
	x=
	l=rewriter()


