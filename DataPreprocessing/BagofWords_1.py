#Bag of words python tutorial

import nltk
nltk.download('punkt')
import numpy as np
import re
import pandas as pd
import heapq

def main():
    text = "Beans. I was trying to explain to somebody as we were flying in, that’s corn. That’s beans. And they were very impressed at my agricultural knowledge. Please give it up for Amaury once again for that outstanding introduction. I have a bunch of good friends here today, including somebody who I served with, who is one of the finest senators in the country, and we’re lucky to have him, your Senator, Dick Durbin is here. I also noticed, by the way, former Governor Edgar here, who I haven’t seen in a long time, and somehow he has not aged and I have. And it’s great to see you, Governor. I want to thank President Killeen and everybody at the U of I System for making it possible for me to be here today. And I am deeply honored at the Paul Douglas Award that is being given to me. He is somebody who set the path for so much outstanding public service here in Illinois. Now, I want to start by addressing the elephant in the room. I know people are still wondering why I didn’t speak at the commencement."

    dataset = nltk.sent_tokenize(text)

    #print("before dataset:",dataset)
    for i in range(len(dataset)):
        dataset[i] = dataset[i].lower() 
        dataset[i] = re.sub(r'\W', ' ', dataset[i]) 
        dataset[i] = re.sub(r'\s+', ' ', dataset[i]) 

    print("after dataset:",dataset,len(dataset)) 
    

    word2count = {}
    for data in dataset: 
        words = nltk.word_tokenize(data)

        for word in words: 
                if word not in word2count.keys(): 
                    word2count[word] = 1
                else: 
                    word2count[word] += 1
    
    
    
    print(word2count)

    k = word2count.keys() # a list of the dict keys
    v = word2count.values() # a list of the dict values

    df = pd.DataFrame(list(zip(k, v)),columns =['words', 'count'])
    df.to_csv("word_count.csv")

    freq_words = heapq.nlargest(100, word2count, key=word2count.get)

    print("freq_words:",freq_words)
    X = [] 
    for data in dataset: 
        vector = [] 
        for word in freq_words: 
            if word in nltk.word_tokenize(data): 
                vector.append(1) 
            else: 
                vector.append(0) 
        X.append(vector) 
    X = np.asarray(X)

    print(X,X.shape)
if __name__=="__main__":
    main()