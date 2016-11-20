'''
Sushrith Arkal
01FB14ECS262
Sec E, 5th Sem
PES University

Script to find words in two courses, get the common
words and find the fraction of common words.
'''

import nltk as nlp
from nltk.stem.snowball import SnowballStemmer
import PyPDF2
import os

def get_stopwords(stopfile):
	# get the stopwords
	stopwords = set(nlp.corpus.stopwords.words('english'))
	stopwords += set([',', ':', '.','!', '?', ';', '\'', '"', '&', '@', '^', '$', '<', '>', '(', ')', '{', '}', '~', '`', 'etc'])
	for stop in stopfile:
		stopwords.add(stop.strip())
	return stopwords

def get_top_n(folder, n, proportion = True, need_to_stem = False, stopwords = set(nlp.corpus.stopwords.words('english'))): #takes the folder containing the pdf files

	lecture_files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and os.path.splitext(os.path.join(folder, f))[-1] == '.pdf']

	document = b''
	for lecture in lecture_files:
		file = open(os.path.join(folder, lecture), 'rb')
		pdfReader = PyPDF2.PdfFileReader(file)
		#loop through each page
		lec_doc = b''
		for i in range(pdfReader.numPages):
			page = pdfReader.getPage(i)
			text = page.extractText()
			lec_doc += text.encode("ascii", "ignore") # replace with utf-8 if needed
		document += lec_doc
	## clean the document byte object

	# convert to string
	document = document.decode('ascii').replace('\n', '')
	document = document.lower()

	# tokenise into words
	tokens = nlp.tokenize.word_tokenize(document)


	# remove stop words
	# can do more stuff here
	tokens = [token for token in tokens if token not in stopwords]

	# stem words
	if need_to_stem:
		stemmer = SnowballStemmer("english")
		tokens = [stemmer.stem(token) for token in tokens]

	#find freq dist
	fdist = nlp.probability.FreqDist(tokens)

	#print n most common words
	print('processed ' + folder)
	len_tok = len(tokens)
	if proportion:
		print(len_tok)
		print(int(len_tok*n))
		print('\n'.join([str(tup) for tup in fdist.most_common(int(len_tok*n))]))
		return len_tok, set(fdist.most_common(int(len_tok * n)))
	else:
		print('\n'.join([str(tup) for tup in fdist.most_common(n)]))
		return len_tok, set(fdist.most_common(n))

stopwords = get_stopwords(open('stopwords'))

num_core, core = get_top_n('high-perf-comp', 100, False, True, stopwords)
num_prereq, prereq = get_top_n('comp-netw', 100, False, True, stopwords)

prereq_set = set([t[0] for t in prereq])
core_set = set([t[0] for t in core])

int_set = prereq_set & core_set # get intersection
num_common = len(int_set)

print('num intersect words:', num_common)
#print('intersection: ', int_set)
print('num of words in prereq:', num_prereq)
print((num_common/num_prereq) * 100) #fraction of dependency
