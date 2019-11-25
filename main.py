from rewriter import syno
import re
import nltk
# string = input("Enter some text1: ")
def synonyms(word_list,i):
    # no_specials_string = re.sub('[#,:";]', '', string)
    # sentences=re.split('\? |\?|\. |\.|! |!',no_specials_string)
    # sentences.pop();
    # #print(sentences)
    # left = {}
    # right = {}
    # words = []
    word = word_list[i]
    tags = ['NN','NNS','JJ','JJR','JJS','FW','RB','RBR','RBS']
    tags_v = ['VB','VBD','VBG','VBN','VBP','VBZ']
    helping_verbs=['am', 'is', 'are', 'was', 'were', 'be', 'being','been',
                'will', 'would', 'shall', 'should', 'may', 'might', 'must', 'can','could',
                'do', 'does','did','have','having','has','had']
    # for sentence in sentences:
        #word_list = sentence.split()
    n = len(word_list)
    #i = 0
    #print(word_list)
    #for word in word_list:
    if i == 0:
        left = ""
        right = word_list[i+1]
    
    elif i == n-1:
        left = word_list[i-1]
        right = ""
        
    else:
        left = word_list[i-1]
        right = word_list[i+1]
    # print(left,right)    
    y=nltk.pos_tag(nltk.word_tokenize(" ".join(word_list)))
    for word1,pos in y:
        # print(word1)
        if word1 == word:
            # print(word)
            word_lower = word1.lower()
            if pos in tags:
                # print("hey")
                syno_list = syno(left,word,right)
                return syno_list
                
            elif pos in tags_v:
                # print("heya")
                if word_lower not in helping_verbs:
                    # print("heyaa")
                    syno_list = syno(left,word,right)
                    return syno_list
    return []
# print(words)
# print(left)
# print(right)
 
    # for word,pos in nltk.pos_tag(nltk.word_tokenize(str(word))):
    #     word_lower = word.lower()
    #     if pos in tags:
    #         words.append(word)
    #     elif pos in tags_v:
    #         if word_lower not in helping_verbs:
    #             words.append(word)
    
       
       


# for word in list(dict.fromkeys(words)):
#     # print(word)
#     # print(left[word])
#     # print(right[word])
#     syno_list = syno(left[word],word,right[word])
#     # print("recieved")
#     # print(syno_list)
#     if syno_list:
#         print("Suggested list of synonyms for "+word+" "+str(syno_list))