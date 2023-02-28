from collections import Counter
import numpy as np
from sklearn.naive_bayes import MultinomialNB
import math

import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
import glob
import os

def extract_features(direct):
 Path = 'C:/Users/cool dude/PycharmProjects/hello/hw9 (1)/'
 Allwords = []
 #features_matrix = []
 all_words = []
 features_matrix = np.array([[1],[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]])

 with open('C:/Users/cool dude/PycharmProjects/hello/hw9 (1)/'+direct, 'r') as fin:
    mylist = [line.rstrip('\n') for line in fin]


    train_labels = np.zeros(len(mylist))
    docID = 0;


    for x in mylist:

        if x.endswith(".txt"):
            # print(x)
                #features_maaltrix.reshape(-1, 1)
                with open(Path + x, "r", encoding=None) as y:
                    for line in y:
                        words = line.split()
                        all_words += words

        train_labels[docID] = 0;
        filepathTokens = x.split('/')
        lastToken = filepathTokens[len(filepathTokens) - 1]

        if lastToken.startswith("con"):
          train_labels[docID] = 1;
          print("L")
          docID = docID + 1
         # print(features_matrix[docID])
        if lastToken.startswith("lib"):
           # features_matrix.append(lastToken)

            train_labels[docID] = 0;
            print("C")

    dictionary = Counter(all_words)


 return features_matrix,train_labels

def topwords(trainData):
     Path = 'C:/Users/cool dude/PycharmProjects/hello/hw9 (1)/'
     all_Words = []

     all_words = []
     with open('C:/Users/cool dude/PycharmProjects/hello/hw9 (1)/' + trainData, 'r') as fin:
         mylist = [line.rstrip('\n') for line in fin]


         train_labels = np.zeros(len(mylist))
         docID = 0;

         for x in mylist:
             if (x.endswith(".txt"))&(x.startswith("lib")):
                 # print(x)
                 # features_maaltrix.reshape(-1, 1)
                 with open(Path + x, "r", encoding=None) as y:
                     for line in y:

                         words = line.split()
                         #print(words.mos)
                         all_words += words
                 Prob_Total_Con =len(all_words)
                 filepathTokens = x.split('/')
                 lastToken = filepathTokens[len(filepathTokens) - 1]
         dictionary=Counter(all_words)
         Common_lib =dictionary.most_common(20)
        # print(Common_Con[0].__getitem__(1))

         for MostCommonlibWord in Common_lib:
             prob=MostCommonlibWord.__getitem__(1)
             WordName = MostCommonlibWord.__getitem__(0)
             Prob_LibWord= prob / Prob_Total_Con
             print("liberal "+WordName+" "+('{0:.04f}'.format(Prob_LibWord)))
         for z in mylist:

             if (z.endswith(".txt")) & (z.startswith("con")):
                 # features_maaltrix.reshape(-1, 1)
                 with open(Path + z, "r", encoding=None) as k:
                     for line in k:
                         words = line.split()
                         # print(words.mos)
                         all_Words += words
                 Prob_Total_Con = len(all_Words)
                 filePathTokens = z.split('/')
                 lastToken = filePathTokens[len(filePathTokens) - 1]
         dictionary = Counter(all_Words)
         Common_Con = dictionary.most_common(20)
         for MostCommonWord in Common_Con:
             Prob=MostCommonWord.__getitem__(1)
             Wordname = MostCommonWord.__getitem__(0)
             Prob_ConWord= Prob / Prob_Total_Con
             print("conservative " + Wordname + " " + ('{0:.04f}'.format(Prob_ConWord)))

     return

def stopwords(trainData,stopwords):
    Path = 'C:/Users/cool dude/PycharmProjects/hello/hw9 (1)/'
    OtherWords = []
    StopWords=[]
    all_words = []
    with open('C:/Users/cool dude/PycharmProjects/hello/hw9 (1)/' + trainData, 'r') as fin:
        mylist = [line.rstrip('\n') for line in fin]

        for x in mylist:
            if (x.endswith(".txt")):
                with open(Path + x, "r", encoding=None) as y:
                    for line in y:
                        words = line.split()
                        # print(words.mos)
                        all_words += words
                Prob_Total_Con = len(all_words)
                filepathTokens = x.split('/')
                lastToken = filepathTokens[len(filepathTokens) - 1]
        dictionary = Counter(all_words)
        CommonStopwords = dictionary.most_common(stopwords)
        for a in CommonStopwords:
            StopWords.append(a.__getitem__(0))
        f = open("C:/Users/cool dude/PycharmProjects/hello/hw9 (1)/nbStopWords.txt", mode='w')
        for x in mylist:
            if (x.endswith(".txt")):

                with open(Path + x, "r", encoding=None) as y:
                    for line in y:
                        #words = line.split()
                        if not line in StopWords:

                            OtherWords.append(line)

                            f.write(line)
    return

def  programtopwordsLogOdds(trainData):
    Path = 'C:/Users/cool dude/PycharmProjects/hello/hw9 (1)/'
    all_words = []
    all_words_con = []
    Prob_con = []
    all_words_lib = []
    Prob_lib = []
    LogOddsRatio=[]
    LogOddsRatioRev=[]
    Word_con=[]
    Word_lib=[]
    LogOddsWordName=[]
    with open('C:/Users/cool dude/PycharmProjects/hello/hw9 (1)/' + trainData, 'r') as fin:
        mylist = [line.rstrip('\n') for line in fin]
        for x in mylist:
            # print('C:/Users/cool dude/PycharmProjects/hello/hw9 (1)/'+line)

            if x.endswith(".txt"):
                # print(x)
                # features_maaltrix.reshape(-1, 1)
                with open(Path + x, "r", encoding=None) as y:
                    for line in y:
                        words = line.split()
                        all_words += words
                y.close()
            if (x.endswith(".txt")) & (x.startswith("lib")):
                with open(Path + x, "r", encoding=None) as z:
                    for line in z:
                        Words = line.split()
                        all_words_lib += Words
                    z.close()

            if (x.endswith(".txt")) & (x.startswith("con")):
                with open(Path + x, "r", encoding=None) as p:
                    for line in p:
                        Words = line.split()
                        all_words_con += Words
                    p.close()
        dictionary = Counter(all_words_con)
        ConWords = dictionary.most_common()
        #print(ConWords)
        for f in ConWords:
            Prob_con.append(f.__getitem__(1))
            Word_con.append(f.__getitem__(0))
        TotalAllWords=len(all_words)
        dictionary = Counter(all_words_lib)
        LibWords = dictionary.most_common()
        # print(LibWords)
        for e in LibWords:
            Prob_lib.append(e.__getitem__(1))
            Word_lib.append(e.__getitem__(0))

    if(len(Word_con)>len(Word_lib)):
        rng=len(Word_lib)
    else:
        rng=len(Word_con)
    for i in range(rng):

                LibValue = Prob_lib[i]
                ConValue = Prob_con[i]

                LogOddsRatio.append('{0:.04f}'.format(math.log(LibValue/ConValue,2)))
                LogOddsRatioRev.append('{0:.04f}'.format(math.log(ConValue/LibValue,2)))
                LogOddsWordName.append(Word_lib[i])
    # LogOddsRatio=sorted(LogOddsRatio,reverse=True)
    #print(LogOddsRatio[0:20])
    Z = [x for y, x in sorted(zip(LogOddsRatio, LogOddsWordName),reverse=True)]
    print(Z[0:20])
    M = [x for y, x in sorted(zip(LogOddsRatioRev, LogOddsWordName), reverse=True)]
    print(M[0:20])
    return

    #print(dictionary)
Train="split.train"
Test="split.test"

print("Answer to Question 1:")
features_matrix,labels_train = extract_features(Train)
print("")
print("Answer to Question 2:")
features = topwords(Train)
print("")
print("Answer to Question 3:")
features_matrix = stopwords(Train,10)
print("Words after excluding stop words have been saved to nbStopWords.txt ")
print("")
print("Answer to Question 5:")
features_matrix = programtopwordsLogOdds(Train)

model = MultinomialNB()
#model.fit(features_matrix,labels_train)

# def extract_features(root_dir):
#     with open('C:/Users/cool dude/PycharmProjects/hello/hw9 (1)/split.test', 'r') as fin:
#         mylist = [line.rstrip('\n') for line in fin]
#        #features_matrix = np.zeros((len(mylist), 3000))
#         train_labels = np.zeros(len(mylist))
#         print(train_labels)
#
#         for x in mylist:
#             if x.endswith(".txt"):
#                 with open(Path + x, "r", encoding=None) as y:
#                     for line in y:
#                         words = line.split()
#                         for word in words:
#                             wordID = 0
#                             for i,d in enumerate(dictionary):
#                                 if d[0] == word:
#                                     wordID = i