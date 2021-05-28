import re
import csv
import pickle
import csv
import math
import pylabeador
import collections
import sys


csv.field_size_limit(sys.maxsize)
#pylabeador.syllabify("abogado")

x=0


Row=[]
with open('gender.trigger', 'r',encoding='utf-8') as csv_file:
	csv_reader = csv.reader(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
	line_count = 0

	for row in csv_reader:
		
		Row.append(row[0].lower())
'''
with open('overtime.trigger', 'r',encoding='utf-8') as csv_file:
	csv_reader = csv.reader(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
	line_count = 0

	for row in csv_reader:
		
		Row.append(row[0].lower())		


with open('annleave.trigger', 'r',encoding='utf-8') as csv_file:
	csv_reader = csv.reader(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
	line_count = 0

	for row in csv_reader:
		
		Row.append(row[0].lower())
'''
f=open('all_binds_languages.pkl','rb')
text=[]

text=[]
langs=[]
country={}
x=0
from nltk.corpus import cmudict
CMUdict = cmudict.dict()      #syllable
def syllableCount_en(word):      #returns count of syllables in word using CMU's dictionary, or none if token isn't a word
	'''
	Counts the number of syllable in a given word
	'''
	if word==-1:
		return('syllabeCount')
	word=word.lower()
	if word in CMUdict:
		return[len([y for y in x if y[-1].isdigit()]) for x in CMUdict[word.lower()]][0]
		#return(len(CMUdict[word][0]))
	else:
		return(-1)

def isComplex(word):        #Is word Complex
	'''
	Returns True if word is complex
	i.e. syllable count >3
	
	'''
	if word==-1:
		return('isComplex')
	if syllableCount_en(word) >=3:
		return True
	elif syllableCount_en(word)<0:
		return(None)
	else:
		return(False)


def ARI(text,lang='en'):
	sentence=len(text.split('. '))
	text=text.replace('. ',' ')
	chars=len(text.replace(' ',''))
	words=len(text.split(' '))
	#if lang=='en':
	return(4.71*(chars/words)+0.5*(words/sentence)-21.43)

def CLI(text,lang='en'):
	sentence=len(text.split('. '))
	text=text.replace('. ',' ')
	
	chars=len(text.replace(' ',''))
	words=len(text.split(' '))
	#0.0588L-0.296S-15.8
	#if lang=='en':
	L=100*chars/words
	S=100*sentence/words
	return(0.0588*L-0.296*S-15.8)		

def lexicalDensity(text):
	text=text.replace('. ',' ')
	text=text.split(' ')
	return(len(set(text))/len(text))
def flesch(text,lang):
	sentence=len(text.split('. '))
	text=text.replace('. ',' ')
	
	words=len(text.split(' '))

	wordSet=text.split(' ')
	if lang=='en':
		syllables=0
		for w in wordSet:
			syllCount=syllableCount_en(w)
			if syllCount != -1:
				syllablse=syllCount+syllables
		return(206.835-1.015*(words/sentence)-84.6*(syllables/words))
	else:

		syllables=0
		for w in wordSet:
			try:
				syllCount=len(pylabeador.syllabify(w))
			
				syllables=syllCount+syllables
			except:
				syllables=syllables
		if lang=='it':		
			return(217-(1.3*(words/sentence))-(0.6*(syllables/words)))
		else:
			return(217-(1.3*(words/sentence))-(0.6*(syllables/words)))		
#{\displaystyle F=217-(1,3*S)-(0,6*P)}		
def LIX(text):
	sentence=len(text.split('. '))
	text=text.replace('. ',' ')
	
	words=len(text.split(' '))
	wordSet=text.split(' ')
	longWord=0
	for w in wordSet:
		if len(w)>6:
			longWord+1
	return(words/sentence+(longWord*100)/words)

def simpson(text):
	text=text.replace('. ',' ')
	
	words=len(text.split(' '))
	

	denom=words*(words-1)
	numer=len(set(text.split(' ')))
		
	return(1-numer/denom)

def hapaxLegomena(text):
	text=text.replace('. ',' ')
	
	words=text.split(' ')

	counter=dict(collections.Counter(words))
	numer=0
	for c in counter:
		if counter[c]==1:
			numer=numer+1
	return(numer/len(words))
	return(count)     		
def yule(text):
	text=text.replace('. ',' ')
	
	words=text.split(' ')
	freqs=list(dict(collections.Counter(words)).values())
	Vi=dict(collections.Counter(freqs))       #Words Occuring i times
	M=0
	for v in Vi:
		M=M+(v**2)*Vi[v]
	N=len(words)
	K=1000*(M-N)/(N**2)
	return(K)

def SMOG(text,lang='en'):

	text=text.replace('\n','. ')
	while(text.find('. . ')>-1):
		text=text.replace('. . ','. ')					
	text=text.split('. ')
	text2=[]
	text=text.replace('-',' ')
	for t in text:
		t = re.sub(r'[^\w\s]','',t).lower()
		text2.append(t)
	text='. '.join(text2)	
	sentence=len(text.split('.'))
	text=text.lower()

	while(text.find('  ')>-1):
		text=text.replace('  ',' ')
	chars=len(text.replace(' ',''))
	text = re.sub(r'[^\w\s]','',text).lower()
	words=len(text.split(' '))
	wordSet=text.split(' ')


	complexWords=0
	for w in wordSet:
		
		if isComplex(w)==True:
			complexWords=complexWords+1
	smog=1.0430*math.sqrt(complexWords*(30/sentence))+3.1291
	return(smog)
measure={}
with open('cba_texts_01072020.csv', 'r',encoding='utf-8') as csv_file:
	csv_reader = csv.reader(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
	line_count = 0
	for row in csv_reader:
		
		if x>0:
			
		

			#if row[1]=='united-kingdom':
			#langs.append(row[3])
			lang=row[3].split('_')[0].lower()
			if lang=='en' or lang=='it' or lang=='es':
				if row[0] not in measure:

					measure[row[0]]={}
					measure[row[0]]['flesch']=[]
					measure[row[0]]['lexDens']=[]
					measure[row[0]]['ari']=[]
					measure[row[0]]['cli']=[]
					measure[row[0]]['lix']=[]
					measure[row[0]]['hapax']=[]
					measure[row[0]]['simpson']=[]
					measure[row[0]]['wordCount']=[]
					measure[row[0]]['unique']=[]
					measure[row[0]]['yuleK']=[]
					measure[row[0]]['ln']=lang
				
				textSet=row[4].split('</p>')					
				for text in textSet:
					textOrig=text
					text=text.replace('\n','. ')
				
					text=text.replace('-',' ')
				
					TAG_RE = re.compile(r'<[^>]+>')


					text=TAG_RE.sub('', text)




					while(text.find('. . ')>-1):
						text=text.replace('. . ','. ')					
					text=text.split('. ')
					text2=[]
					for t in text:
						t = re.sub(r'[^\w\s]','',t).lower()
						text2.append(t)
					text='. '.join(text2)
					while(text.find('  ')>-1):
						text=text.replace('  ',' ')
					while(text.find('. . ')>-1):
						text=text.replace('. . ','. ')					
					
					if len(text.split(' '))>7:
						measure[row[0]]['wordCount'].append(len(text.split(' ')))
						measure[row[0]]['unique'].append(len(set(text.split(' '))))
						measure[row[0]]['flesch'].append(flesch(text,lang))
						measure[row[0]]['lexDens'].append(lexicalDensity(text))
						measure[row[0]]['ari'].append(ARI(text))
						measure[row[0]]['cli'].append(CLI(text))
						measure[row[0]]['lix'].append(LIX(text))
						measure[row[0]]['hapax'].append(hapaxLegomena(text))
						measure[row[0]]['simpson'].append(simpson(text))
					
						measure[row[0]]['yuleK'].append(yule(text))
						
			else:
				if row[0] not in measure:

					measure[row[0]]={}
					measure[row[0]]['lix']=[]
					measure[row[0]]['wordCount']=[]
					measure[row[0]]['ln']=lang

					measure[row[0]]={}
					
					measure[row[0]]['lexDens']=[]
					measure[row[0]]['ari']=[]
					measure[row[0]]['cli']=[]
					measure[row[0]]['lix']=[]
					measure[row[0]]['hapax']=[]
					measure[row[0]]['simpson']=[]
					measure[row[0]]['wordCount']=[]
					measure[row[0]]['unique']=[]
					measure[row[0]]['yuleK']=[]
					measure[row[0]]['ln']=lang
			
				textSet=row[4].split('</p>')					
				for text in textSet:
					textOrig=text
					text=text.replace('\n','. ')
					text=text.replace('-',' ')

					TAG_RE = re.compile(r'<[^>]+>')


					text=TAG_RE.sub('', text)




					while(text.find('. . ')>-1):
						text=text.replace('. . ','. ')					
					text=text.split('. ')
					text2=[]
					for t in text:
						t = re.sub(r'[^\w\s]','',t).lower()
						text2.append(t)
					text='. '.join(text2)
					while(text.find('  ')>-1):
						text=text.replace('  ',' ')
					while(text.find('. . ')>-1):
						text=text.replace('. . ','. ')					
					
					if len(text.split(' '))>7:
						measure[row[0]]['wordCount'].append(len(text.split(' ')))
						measure[row[0]]['unique'].append(len(set(text.split(' '))))
						measure[row[0]]['lexDens'].append(lexicalDensity(text))
						measure[row[0]]['ari'].append(ARI(text))
						measure[row[0]]['cli'].append(CLI(text))
						measure[row[0]]['lix'].append(LIX(text))
						measure[row[0]]['hapax'].append(hapaxLegomena(text))
						measure[row[0]]['simpson'].append(simpson(text))
					
						measure[row[0]]['yuleK'].append(yule(text))
						
							
		x=x+1		

ROW=['ln','flesch','ari','cli','lix','lexDens','simpson','hapax','yuleK']
import numpy as np 

csv_file=open('Complexity.csv','w', encoding="utf-8")
Res2={}
res={}
meas={}
writer=csv.writer(csv_file,delimiter=',', lineterminator='\n')     
writer.writerow(['cba','language','fleschKincaid','ARI','CLI','LIX','STTR','Simpson Index','Hapax Legomena',"Yule's K",'wordCount','uniqueWords'])
for row in measure:
	X=[]
	X.append(row)
	if row not in Res2:
		Res2[row]={}
	if measure[row]['ln'] not in Res2[row]:
		Res2[row][measure[row]['ln']]={}
	for r in ROW:

		if r in measure[row]:
			if type(measure[row][r])!=str:

				if r not in meas:
					meas[r]={}
				if measure[row]['ln'] not in meas[r]:
					meas[r][measure[row]['ln']]={}
				if row not in meas[r][measure[row]['ln']]:
					meas[r][measure[row]['ln']][row]=np.mean(measure[row][r])
				

				X.append(np.mean(measure[row][r]))
				if r not in res[lang]:
					res[lang][r]=[]
					
				if r not in Res2[row][measure[row]['ln']]:
					Res2[row][measure[row]['ln']][r]=np.mean(measure[row][r])
				res[lang][r].append(np.mean(measure[row][r]))
			else:
				X.append(measure[row][r])
				lang=measure[row][r]

				if measure[row][r] not in res:
					res[lang]={}				
		else:
			X.append('')

	X.append(np.mean(measure[row]['wordCount']))
	X.append(np.mean(measure[row]['unique']))
	if 'wordCount' not in res[lang]:
		res[lang]['wordCount']=[]

	if 'unique'	not in res[lang]:
		res[lang]['unique']=[]
	
	
	res[lang]['wordCount'].append(np.mean(measure[row]['wordCount']))
	res[lang]['unique'].append(np.mean(measure[row]['unique']))
	Res2[row][measure[row]['ln']]['wordCount']=np.mean(measure[row]['wordCount'])
	Res2[row][measure[row]['ln']]['unique']=np.mean(measure[row]['unique'])


	writer.writerow(X)


CenTen={}
for l in res:
	if l not in CenTen:
		CenTen[l]={}
	for item in res[l]:
		CenTen[l][item]=[np.mean(res[l][item]),np.std(res[l][item])]
		#print(l,item,np.mean(res[l][item]),np.std(res[l][item]))

for row in Res2:
	for l in Res2[row]:
		for item in Res2[row][l]:
				#print(row,item,Res2[row][l][item],(Res2[row][l][item]-CenTen[l][item][0])/CenTen[l][item][0])
				if (Res2[row][l][item]-CenTen[l][item][0])/CenTen[l][item][0]>1.95:
					S=5
				elif (Res2[row][l][item]-CenTen[l][item][0])/CenTen[l][item][0]<-1.95:
					S=0
				elif (Res2[row][l][item]-CenTen[l][item][0])/CenTen[l][item][0]>0.67:	
					S=4

				elif (Res2[row][l][item]-CenTen[l][item][0])/CenTen[l][item][0]<-0.67:
					S=1
				elif (Res2[row][l][item]-CenTen[l][item][0])/CenTen[l][item][0]<0:
					S=3
				
				else:
					S=2
				#if S==5:
					#print(XXX)
				#print(row,item,Res2[row][l][item],S)

meas2={}
for m in meas:
	meas2[m]={}
	for lang in meas[m]:
		meas2[m][lang]={}

		Sort=sorted(meas[m][lang].items(),key=lambda x:x[1])
		if len(Sort)>5:
			quin1=Sort[int(len(Sort)/5)-1][1]
			quin2=Sort[int(2*len(Sort)/5)-1][1]
			quin3=Sort[int(3*len(Sort)/5)-1][1]
			quin4=Sort[int(4*len(Sort)/5)-1][1]
			
			
			meas2[m][lang] = [quin1, quin2,quin3,quin4]
		else:
			meas2[m][lang] =[Sort[int(1*len(Sort)/2)-1][1]]
			

csv_file=open('ranked_Sep.csv','w', encoding="utf-8")

writer=csv.writer(csv_file,delimiter=',', lineterminator='\n')     
writer.writerow(['cba','language','fleschKincaid','ARI','CLI','LIX','STTR','Simpson Index','Hapax Legomena',"Yule's K",'wordCount','uniqueWords'])

for row in measure:
	X=[]
	X.append(row)
	for r in ROW:

		if r in measure[row]:
			if type(measure[row][r])!=str:
				if len(meas2[r][lang])>3:
					if np.mean(measure[row][r])<meas2[r][lang][0]:
						S=5 
					
					elif np.mean(measure[row][r])<meas2[r][lang][1]:
						S=4 
					elif np.mean(measure[row][r])<meas2[r][lang][2]:
						S=3 
					elif np.mean(measure[row][r])<meas2[r][lang][3]:
						S=2 
					else:
						S=1
				else:
					if np.mean(measure[row][r])<meas2[r][lang][0]:
						S=5 
					else:
						S=1	
				X.append(S)	
			else:
				lang=measure[row][r]
				X.append(lang)
				
		else:
			X.append('')
	writer.writerow(X)


csv_file=open('accessibility.csv','w', encoding="utf-8")

writer=csv.writer(csv_file,delimiter='\t', lineterminator='\n')     
writer.writerow(['cba','language','readability','diveristy','accessibility'])

scores={}
x=0
with open('ranked_Sep.csv', 'r',encoding='utf-8') as csv_file:
	csv_reader = csv.reader(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
	line_count = 0
	for row in csv_reader:
		
		if x>0:
			read=[]
			cmplx=[]
			acces=[]
			for r in range(2,6):
				if row[r] !='':
					read.append(int(row[r]))
			for r in range(6,10):
				if row[r] !='':
					cmplx.append(int(row[r]))

			for r in range(2,10):
				if row[r] !='':
					acces.append(int(row[r]))



			writer.writerow([row[0],row[1],round(np.mean(read),2),round(np.mean(cmplx),2),round(np.mean(acces),2)])
		x=x+1