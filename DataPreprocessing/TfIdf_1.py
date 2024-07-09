'''
tf  : is the number of times a term appears in a particular document. So it’s specific to a document
idf : is a measure of how common or rare a term is across the entire corpus of documents. 
So the point to note is that it’s common to all the documents. 
If the word is common and appears in many documents, the idf value (normalized) will approach 0 or else approach 1 if it’s rare.

tf-idf value of a term in a document is the product of its tf and idf. The higher is the value, the more relevant the term is in that document.

Using sklearn TfIdf vectorizer
'''

from sklearn.feature_extraction.text import TfidfVectorizer


def main():

    d1="petrol cars are cheaper than diesel cars"
    d2="diesel is cheaper than petrol"

    doc_corpus=[d1,d2]
    print(doc_corpus)

    vec=TfidfVectorizer(stop_words='english')

    matrix=vec.fit_transform(doc_corpus)
    
    print("Feature Names ",vec.get_feature_names_out())
    print("index of Feature Names:",vec.vocabulary_)

    print("matrix:",matrix)

    print("Sparse Matrix \n",matrix.shape,"\n",matrix.toarray())

if __name__=="__main__":
    main()