import bs4 as bs
import urllib.request
import re
import nltk
import heapq
import validators
nltk.download('stopwords')


def url_rize(raw_urls,types):
    if types == 'ss':
        thres   = 25
        sen_num = 5
        key_sen = 2
    elif types == 'ls':
        thres   = 29
        sen_num = 7
        key_sen = 4
    else:
        thres   = 32
        sen_num = 15
        key_sen = 7
    valid = validators.url(raw_urls)
    if valid == True:
        url = raw_urls
       
        source = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(source,'lxml')
        text = ""
        title = soup.find('title').text
        for paragraph in soup.find_all('p'):
            text += paragraph.text
    else:
        text = raw_urls
       
    text = re.sub(r'\[[0-9]+\]',' ',text)
    text = re.sub(r'\s+',' ',text)
    clean_text = text.lower()
    clean_text = re.sub(r'\W',' ',clean_text)
    clean_text = re.sub(r'\d',' ',clean_text)
    clean_text = re.sub(r'\s+',' ',clean_text)

    sentences = nltk.sent_tokenize(text)
    stop_words = nltk.corpus.stopwords.words('english')

    word2count = {}
    for word in nltk.word_tokenize(clean_text):
        if word not in stop_words:
            if word not in word2count.keys():
                word2count[word]=1
            else:
                word2count[word] += 1

    for key in word2count.keys():
        word2count[key] = word2count[key]/max(word2count.values()) 
        
    sent2score = {} 

    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()): 
            if word in word2count.keys():
                if len(sentence.split(' ')) < thres:
                    if sentence not in sent2score.keys():
                        sent2score[sentence] = word2count[word]
                    else:
                        word2count[word] += word2count[word]                 
    best = heapq.nlargest(sen_num,sent2score,key=sent2score.get)
    sents2score = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()): 
            if word in word2count.keys():
                if len(sentence.split(' ')) < 20:
                    if sentence not in sents2score.keys():
                        sents2score[sentence] = word2count[word]
                    else:
                        word2count[word] += word2count[word] 
    key_points = heapq.nlargest(key_sen,sents2score,key=sents2score.get)
    x = " ".join(best)
    if valid == True:
        return [x,title,key_points]
    else:
        return[x,'Summary',key_points]

