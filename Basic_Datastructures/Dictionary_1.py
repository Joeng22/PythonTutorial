#Python dictionary tutorial

def DefaultDictionary():
    dict1 = {"Country":"India","State":"Karnataka","Pin":560122}
    print(dict1)

def GetLetterCountInWord(word1):
    dict1 = {}
    #Convert upper case letters to lower case
    word1 = word1.lower()

    for each in word1:
        if each == " ":
            continue
        if each in dict1:
            dict1[each]=dict1[each]+1
        else:
            dict1[each] = 1
    return dict1


    

if __name__=="__main__":
    DefaultDictionary()
    word1 = "United states of America"
    dictionary = GetLetterCountInWord(word1)
    print(dictionary)