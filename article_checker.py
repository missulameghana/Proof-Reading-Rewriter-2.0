import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from pattern.en import referenced
wnl=WordNetLemmatizer()
wnl.lemmatize('better','a')

var = input("Enter some text:" )
i=0;
# vowels=['A','E','I','O','U']
count=0;
lines=re.split('\? |\?|\. |\.|! |!',var);

for x in lines:
    if(i!=len(lines)-1):
        x1=x.split(" ");
        # print(x1)
        count=0;
        for w in x1:
            count=count+1
            # print(w)
            if(w=="a" or w=="A"):
                word = x1[count].lower()
                # l=arpabet[word][0]
                # p=l[0][0]
            #     if p in vowels:
            #         s="Would u like to change "+w+" "+word+" to an "+word+"?"
            #         reply=input(s)
            # elif (w=="an" or w=="An"):
            #     word = x1[count].lower()
            #     l=arpabet[word][0]
            #     p=l[0][0]
            #     if p not in vowels:
            #         s="Would u like to change "+w+" "+word+" to a "+word+"?"
            #         reply=input(s)

    i=i+1;

def check_article(s):

