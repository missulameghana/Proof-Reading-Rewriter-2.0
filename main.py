from rewriter import syno
import re
string = input("Enter some text: ")
no_specials_string = re.sub('[!#?,.:";]', '', string)
words = no_specials_string.split()
#print(words)
for word in words:
	syno_list = syno(word)
	#print(syno_list)
	if syno_list:
		print("Suggested list of synonyms for "+word+" "+str(syno_list)) 