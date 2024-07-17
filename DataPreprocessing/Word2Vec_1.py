import nltk
import gensim

from nltk import sent_tokenize,word_tokenize
import warnings

warnings.filterwarnings(action='ignore')

def main():
    sample = open("Alice.txt")
    s = sample.read()
    print("type s:",type(s),id(s))
    f = s.replace("\n"," ")
    print("type f :",type(f),id(f))

    data = []
    
    # iterate through each sentence in the file
    for i in sent_tokenize(f):
        temp = []
    
        # tokenize the sentence into words
        for j in word_tokenize(i):
            temp.append(j.lower())
    
        data.append(temp)
    
    # Create CBOW model
    model1 = gensim.models.Word2Vec(data, min_count=1,vector_size=100, window=5)
    # Create Skip Gram model
    model2 = gensim.models.Word2Vec(data, min_count=1, vector_size=100,window=5, sg=1)

    # Print results
    print("Cosine similarity between 'alice' " + "and 'wonderland' - Skip Gram : ",model2.wv.similarity('alice', 'wonderland'))
    print("Cosine similarity between 'alice' " + "and 'alice' - Skip Gram : ",model2.wv.similarity('alice', 'alice'))
    print("Cosine similarity between 'alice' " + "and 'she' - Skip Gram : ",model2.wv.similarity('alice', 'she'))
    

if __name__=="__main__":
    main()