getwd()

setwd("/home/sreedhar/Sem5/DAProject/DSAlgo")

library(tm)

#library(wordcloud)

library(SnowballC)

files <- list.files(pattern = "pdf$")
Rpdf <- readPDF(control = list(text = "-layout"))

docs <- Corpus(URISource(files), 
                       readerControl = list(reader = Rpdf))

#corpus.copy <- docs

#dict <- c("node")


docs <- tm_map(docs, removePunctuation)  

for(j in seq(docs))   
{   
  docs[[j]] <- gsub("/", " ", docs[[j]])   
  docs[[j]] <- gsub("@", " ", docs[[j]])   
  docs[[j]] <- gsub("\\|", " ", docs[[j]])   
}  

docs <- tm_map(docs, removeNumbers)

docs <- tm_map(docs, tolower) 
docs <- tm_map(docs, removeWords, stopwords("english"))  

docs <- tm_map(docs, removeWords, c("department", "email"))

docs <- tm_map(docs, stripWhitespace)   

docs <- tm_map(docs, PlainTextDocument)  
docs <- tm_map(docs, stemDocument,language = "english")

#docs <- tm_map(docs, stemCompletion, dictionary = corpus.copy)  

dtm <- DocumentTermMatrix(docs)  

inspect(dtm)

tdm <- TermDocumentMatrix(docs)  #Transpose

freq <- colSums(as.matrix(dtm))   
length(freq) 

ord <- order(freq)  

dtms <- removeSparseTerms(dtm, 0.1) # This makes a matrix that is 10% empty space, maximum.   
inspect(dtms)  

freq <- colSums(as.matrix(dtms))  

freq <- sort(colSums(as.matrix(dtm)), decreasing=TRUE)

head(freq, 150)

wf <- data.frame(word=names(freq), freq=freq)   




library(ggplot2)   
ggplot(subset(wf, freq>300), aes(word, freq)) + geom_bar(stat="identity") + theme(axis.text.x=element_text(angle=45, hjust=1))   


ggsave("DSAlgo.jpg")
