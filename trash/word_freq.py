import nltk as nlp
from nltk.stem.snowball import SnowballStemmer
import PyPDF2
import os

def get_top_n(folder, n, proportion = True, need_to_stem = False): #takes the folder containing the pdf files
	stopwords = nlp.corpus.stopwords.words('english')
	stopwords += [',', ':', '.','!', '?', ';', '\'', '"', '&', '@', '^', '$', '<', '>', '(', ')', '{', '}', '~', '`']
	lecture_files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and os.path.splitext(os.path.join(folder, f))[-1] == '.pdf']
	#print(lecture_files)
	document = b''
	for lecture in lecture_files:
		file = open(os.path.join(folder, lecture), 'rb')
		pdfReader = PyPDF2.PdfFileReader(file)
		#loop through each page
		#print(lecture, pdfReader.numPages)
		lec_doc = b''
		for i in range(pdfReader.numPages):
			page = pdfReader.getPage(i)
			text = page.extractText()
			#print(text.encode("ascii", "xmlcharrefreplace"))
			lec_doc += text.encode("ascii", "ignore") # replace with utf-8 if needed
		document += lec_doc
	# clean the document byte object
	#print(document.decode('ascii').replace('\n', ''))
	# convert to string
	document = document.decode('ascii').replace('\n', '')
	# tokenise into words
	tokens = nlp.tokenize.word_tokenize(document)
	# stem words
	if need_to_stem:
		stemmer = SnowballStemmer("english")
		tokens = [stemmer.stem(token) for token in tokens]
	#document = ' '.join(tokens)
	
	# remove stop words
	# can do more stuff here
	#for word in stopwords:
	#	document.replace(word, '')
	
	tokens = [token for token in tokens if token not in stopwords or len(token) <= 1 or token.isdigit() or (token.startswith('-') and token[1:].isdigit()) ]

	#find freq dist
	fdist = nlp.probability.FreqDist(tokens)

	#print n most common words
	if proportion:
		print('\n'.join([str(tup) for tup in fdist.most_common(int(len(tokens)*n))]))
	else:
		print('\n'.join([str(tup) for tup in fdist.most_common(n)]))


get_top_n('comp_netw', 100, False, True)