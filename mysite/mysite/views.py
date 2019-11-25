from django.shortcuts import render
from .forms import MyForm
from .forms import forum
from utils.spelling import correction
from django.template import loader
from django.http import HttpResponse
import re
from utils.main import main
from collections import OrderedDict


dickt = {}
dickt2={}
txt_data = ""
def und_sent(sentence):
	dickt = {}	
	words = re.findall(r"[\w']+|[.,!?;]", sentence)
	last_full_stop = len(words) - words[::-1].index('.')
	words = words[:last_full_stop]
	for w in words:
		dickt[w]=correction(w)
			   
	return dickt
def synon(sentence):
	return main(sentence)


def index(request):
	global dickt
	global txt_data
	if request.method == 'POST':
		print("yass")
		if 'pehla' in request.POST:
			myForm = MyForm(request.POST)
			if myForm.is_valid():
				print("hope")
				text_in2 = myForm.cleaned_data['text_in']					
				dickt = und_sent(text_in2)
				dickt2 = synon(text_in2)
				print(dickt)
				print(dickt2)
				form = MyForm(initial = {'text_in': text_in2})			
				foru = forum()			
				context={}	
				context['foru']=foru		
				context['form']=form
				context['dickt']=dickt
				context['dickt2']=dickt2
				template = loader.get_template('index.html')
				return render(request,'index.html',context);
		elif 'dusra' in request.POST:
			myforu = forum(request.POST)
			if myforu.is_valid():
				print("oye")
				text_in2 = myForm.cleaned_data['text_in']
				change = myforu.cleaned_data['c']
				changeto = myforu.cleaned_data['i']
				dickt = OrderedDict([(changeto, v) if k == change else (k, v) for k, v in dickt.items()])
				dickt[changeto]=[]
				form = MyForm(initial = {'text_in': text_in2})
				foru = forum()						
				context={}			
				context['form']=form
				context['dickt']=dickt
				context['dickt2']=dickt2
				context['foru']=foru
				template = loader.get_template('index.html')
				return render(request,'index.html',context);

	else:
		print("else")
		form = MyForm()	
		foru = forum()

	return render(request,'index.html',{'form':form,'foru':foru});


