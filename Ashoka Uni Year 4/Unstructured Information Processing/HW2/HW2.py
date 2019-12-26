import re,random

space = " "
lines = ["i suppose","and having got","not two minutes"]

def readFile(name):
    corpus = (open(name,"r",encoding="utf8")).read()
    return corpus

def textSplit(corpus): #Splits text into words
    corpus  = re.split('[^A-Za-z]+',corpus.lower())
    corpus = list(filter(lambda x: x != "\n",corpus))
    corpus = list(filter(lambda x: x != None,corpus))

    return corpus

def n_grams(corpus,n): #Generates n-grams
    ngrams = []

    for i in range(0,len(corpus)-(n+1)):
        ngrams.append(corpus[i:i+n])

    return ngrams

def freqGrams(ngrams): #Makes primitive Markov chains
    gram_dict = {}

    for gram in ngrams:
        token = space.join(gram[:-1]) #All words except last, sperated by spaces
        end_token = gram[-1]

        if token not in gram_dict: #Create new entries for gram tokens
            gram_dict[token] = {}

        if end_token not in gram_dict[token]: #Create new entries for next word tokens
            gram_dict[token][end_token] = 0

        gram_dict[token][end_token] += 1

    return gram_dict

def nextWord(corpus,gram_dict,n): #Makes a weighted decision to choose the next word

    token = space.join(corpus.split()[-(n-1):])
    options = gram_dict[token].items()

    total = sum(weight for options, weight in options)
    rand = random.uniform(0,total)

    max = 0

    for option, weight in options:
        max = max + weight

        if max>rand:
            return option
    
def sentenceGen(corpus,n,sentences):
    gen_sentences = []

    ngrams = n_grams(corpus,n)
    gram_dict = freqGrams(ngrams)

    for i in range(3): 
        
        sentence_len = 2

        sentence = sentences[i]
        
        for i in range(8):
            sentence = sentence + " " + nextWord(sentence,gram_dict,n)
        
        gen_sentences.append(sentence)
    return gen_sentences

wap = readFile("War and Peace.txt")
totc = readFile("A Tale of Two Cities.txt")

wap = textSplit(wap)
totc = textSplit(totc)

print (sentenceGen(wap,2,lines))
print (sentenceGen(wap,3,lines))

print (sentenceGen(totc,2,lines))
print (sentenceGen(totc,3,lines))
