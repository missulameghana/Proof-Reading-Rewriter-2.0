from main import *
from spelling import *
from gram import *
import re
inp=input("Enter some text:")

# last=len(words)-words[::1].index('.') +1
# words=words[:last]
punct={}
j=0

var=""
for s in inp:
	if j==0 or inp[j-1]=='.' or inp[j-1]=='?' or inp[j-1]=='!':
		var=var+inp[j].upper()
	elif inp[j-1]==" ":
		if inp[j-2]=='.' or inp[j-2]=='?' or inp[j-2]=='!':
			var=var+inp[j].upper()
		else:
			var=var+inp[j]
	else:
		var=var+inp[j]
	j=j+1
# print(var)
Interro=["What","When","Where","Who","Whom","Which","Whose","Why","How","Is","Are","Will","Shall","Has","Have","Had","Was","Were","Isn't","Wasn't","Aren't","Weren't","Hasn't"]
Possessi=["I","My","She","Her","He","His","You","Your","It","It's","We","Our","They","Their"]
asd=var.split(" ")

# start=""
# j=0
# var=""
# for elem in asd:
# 	if j==0 or asd[j-1][len(asd[j-1])-1:len(asd[j-1])]=='.' or asd[j-1][len(asd[j-1])-1:len(asd[j-1])]=='?' or asd[j-1][len(asd[j-1])-1:len(asd[j-1])]=='!':
# 		# print("heya")
# 		start=elem
# 		var=var+" "+asd[j]
# 	elif asd[j][len(asd[j])-1:len(asd[j])]=='.' or asd[j][len(asd[j])-1:len(asd[j])]=='?' or asd[j][len(asd[j])-1:len(asd[j])]=='!':
# 		if start in Interro:
# 			# print(start)
# 			var=var+" "+asd[j][:-1]+'?'
# 		elif start in Possessives:
# 			var=var+" "+asd[j][:-1]+'.'
# 		else:
# 			var=var+" "+asd[j]
# 	else:
# 		var=var+" "+asd[j]
# 	j=j+1
# print(var)
words=re.findall(r"[\w']+|[.!?]",var)
lines=re.split('\? |\?|\. |\.|! |!',var);
lines.pop()
x=-1
j=-1

for line in lines:
	# xyz=[]
	abc=-1
	
	j=j+1
	line=line.split(" ")
	i=x
	for word in line:
		i=i+1
		abc=abc+1
		l=correction(word.lower())
		if len(l)!=0:
			print(" ".join(words))
			print("Suggested list of correct spellings for "+word+" : ",l)
			option=input("Choose one or to ignore type -1 ")
			if int(option)!=-1:
				if int(option)<=len(l):
					# x=dic[word][option+1]
					words[i]=l[int(option)-1]
					line[abc]=words[i]
					# print(line[abc],words[i])
	# print(" ".join(words))
	print(" ".join(words))
	z=x
	abc=-1
	for word in line:
		z=z+1
		abc=abc+1
		# print(line,abc)
		l=article_checker(line,abc)
		if len(l)!=0:
			print(" ".join(words))
			print("Suggested list of articles for "+word+" : ",l)
			option=input("Choose one or to ignore type -1 ")
			if int(option)!=-1:
				if int(option)<=len(l):
					qwe=z
					abcd=abc
					st=l[int(option)-1]
					stlis=st.split(" ")
					for ele in stlis:
						words[qwe]=ele
						line[abcd]=ele
						qwe=qwe+1
						abcd=abcd+1
	print(" ".join(words))

	z=x
	abc=-1
	for word in line:
		z=z+1
		abc=abc+1
		# print(line,abc)
		l=grammar(line,abc)
		if len(l)!=0:
			print(" ".join(words))
			print("Suggested list of verbs for "+word+" : ",l)
			option=input("Choose one or to ignore type -1 ")
			if int(option)!=-1:
				if int(option)<=len(l):
					qwe=z
					abcd=abc
					st=l[int(option)-1]
					stlis=st.split(" ")
					for ele in stlis:
						words[qwe]=ele
						line[abcd]=ele
						qwe=qwe+1
						abcd=abcd+1
	print(" ".join(words))

	z=x
	abc=-1
	for word in line:
		z=z+1
		abc=abc+1
		# print(line,abc)
		l=Demform(line,abc)
		if len(l)!=0:
			print(" ".join(words))
			print("Suggested list of demonstratives for "+word+" : ",l)
			option=input("Choose one or to ignore type -1 ")
			if int(option)!=-1:
				if int(option)<=len(l):
					qwe=z
					abcd=abc
					st=l[int(option)-1]
					stlis=st.split(" ")
					for ele in stlis:
						words[qwe]=ele
						line[abcd]=ele
						qwe=qwe+1
						abcd=abcd+1
	print(" ".join(words))

	z=x
	abc=-1
	for word in line:
		z=z+1
		abc=abc+1
		# print(line,abc)
		l=Whform(line,abc)
		if len(l)!=0:
			print(" ".join(words))
			print("Suggested list of interrogatives for "+word+" : ",l)
			option=input("Choose one or to ignore type -1 ")
			if int(option)!=-1:
				if int(option)<=len(l):
					qwe=z
					abcd=abc
					st=l[int(option)-1]
					stlis=st.split(" ")
					for ele in stlis:
						words[qwe]=ele
						line[abcd]=ele
						qwe=qwe+1
						abcd=abcd+1
	print(" ".join(words))

	z=x
	abc=-1
	for word in line:
		z=z+1
		abc=abc+1
		# print(line,abc)
		l=Prepform(line,abc)
		if len(l)!=0:
			print(" ".join(words))
			print("Suggested list of prepositions for "+word+" : ",l)
			option=input("Choose one or to ignore type -1 ")
			if int(option)!=-1:
				if int(option)<=len(l):
					qwe=z
					abcd=abc
					st=l[int(option)-1]
					stlis=st.split(" ")
					for ele in stlis:
						words[qwe]=ele
						line[abcd]=ele
						qwe=qwe+1
						abcd=abcd+1
	print(" ".join(words))

	z=x
	abc=-1
	for word in line:
		z=z+1
		abc=abc+1
		# print(line,abc)
		l=Possform(line,abc)
		if len(l)!=0:
			print(" ".join(words))
			print("Suggested list of Possessives for "+word+" : ",l)
			option=input("Choose one or to ignore type -1 ")
			if int(option)!=-1:
				if int(option)<=len(l):
					qwe=z
					abcd=abc
					st=l[int(option)-1]
					stlis=st.split(" ")
					for ele in stlis:
						words[qwe]=ele
						line[abcd]=ele
						qwe=qwe+1
						abcd=abcd+1
	print(" ".join(words))

	


	k=x
	abc=-1
	for word in line:
		k=k+1
		abc=abc+1
		# print(line,abc)
		l=synonyms(line,abc)
		if len(l)!=0:
			print(" ".join(words))
			print("Suggested list of synonyms for "+word+" : ",l)
			option=input("Choose one or to ignore type -1 ")
			if int(option)!=-1:
				if int(option)<=len(l):
					# x=dic[word][option+1]
					words[k]=l[int(option)-1]
					print(abc)
					line[abc]=words[k]
	x=k+1


print(" ".join(words))
