import warnings
import pandas as pd
import math


trainPath = 'C:/Users/cool dude/PycharmProjects/hello/example1.csv'
df =pd.read_csv(trainPath, sep=',', header=0, names=['Anti_satellite_test_ban', 'Export_south_africa', 'Party'])
df.Party[df.Party == 'democrat'] =0
df.Party[df.Party == 'republican'] =1
df.Export_south_africa[df.Export_south_africa == 'y'] =1
df.Export_south_africa[df.Export_south_africa == 'n'] =0
df.Anti_satellite_test_ban[df.Anti_satellite_test_ban == 'y'] =1
df.Anti_satellite_test_ban[df.Anti_satellite_test_ban == 'n'] =0
nodeCount = 0  # for node id

def entropyCalculator(labels):

    total = labels.shape[0]
    ones = labels.sum().sum()
    #print(labels[labels[labels.columns[0]]==1])
    zeros = total - ones
    if total == ones or total == zeros:
        return 0
    entropy = -(ones / total) * math.log(ones / total, 2) - (zeros / total) * math.log(zeros / total, 2)
    #     print ( "ones : " + str(ones) + "zeros : " + str(zeros) + "entropy : " + str(entropy))
    return entropy


# print(entropyCalculator(df[['Class']]))

def informationGain(featurelabels):
    total = featurelabels.shape[0]
    ones = featurelabels[featurelabels[featurelabels.columns[0]] == 1].shape[0]
    zeros = featurelabels[featurelabels[featurelabels.columns[0]] == 0].shape[0]
    #print(total)
    #print(featurelabels[featurelabels.columns[0]])
    #print(featurelabels[featurelabels[featurelabels.columns[0]] == 0].shape[0])

    parentEntropy = entropyCalculator(featurelabels[['Party']])
    entropyChildWithOne = entropyCalculator(featurelabels[featurelabels[featurelabels.columns[0]] == 1][['Party']])
    entropyChildWithZero = entropyCalculator(featurelabels[featurelabels[featurelabels.columns[0]] == 0][['Party']])
    #     print ("left entropy : " + str(entropyChildWithZero))
    #     print ("right entropy : " + str(entropyChildWithOne))

    #print(parentEntropy)
    #print(entropyChildWithOne)
   #print(entropyChildWithZero)

    infoGain = parentEntropy - (ones / total) * entropyChildWithOne - (zeros / total) * entropyChildWithZero
    return infoGain

def findBestAttribute(data):
    maxInfoGain = -1.0
    for x in data.columns:
        if x == 'Party':
            continue

        #print(x)
        currentInfoGain = informationGain(data[[x, 'Party']])
        #         print(str(currentInfoGain) + " " + x)
        if maxInfoGain < currentInfoGain:
            maxInfoGain = currentInfoGain
            bestAttribute = x
    return bestAttribute,maxInfoGain

bestAttribute,maxInfoGain=findBestAttribute(df)
#print(bestAttribute)

def makeDecisionTree(bestAttribute):
    print("Best Attribute : "+str(bestAttribute) +" with Information gain "+str(maxInfoGain))
    print("")
    print("Decision Tree : ")
    if(bestAttribute=="Anti_satellite_test_ban"):

         #print(df.Anti_satellite_test_ban)
         Anti_Y=df.Anti_satellite_test_ban[df.Anti_satellite_test_ban == 1].sum()
         Anti_N=df.Anti_satellite_test_ban[df.Anti_satellite_test_ban == 0].count()

         Export_Y_Anti_Y=(df.Export_south_africa[df.Anti_satellite_test_ban ==1]==1).sum()
         Export_N_Anti_Y=(df.Export_south_africa[df.Anti_satellite_test_ban ==1]==0).sum()
         Export_Y_Anti_N = (df.Export_south_africa[df.Anti_satellite_test_ban == 0] == 1).sum()
         Export_N_Anti_N = (df.Export_south_africa[df.Anti_satellite_test_ban == 0] == 0).sum()
#         print(df['Party'][df['Party']==1])
         print("Anti_satellite_test_ban :  " + str(Anti_Y) + " Y")
         #Subtree =([df.Export_south_africa[df.Anti_satellite_test_ban ==1]])
         #print(Subtree)
         #print(df[[Subtree, 'Party']])
         #print(df.Party[Subtree[Subtree==1]])
         # Party_y_values=0;
         # for a in Subtree:
         #      if(a==df.Party[df.Party[a]]):
         #          Party_y_values.append(a)


         Random=df[df.Anti_satellite_test_ban==1]
         Random_N=(Random[Random['Export_south_africa']==0])
         Random_Y=(Random[Random['Export_south_africa']==1])
         Party_Y_Y=Random_Y['Party'].sum()
         Party_Y_N=Random_Y['Party'].count()-Party_Y_Y
         Party_N_Y=Random_N['Party'].sum()
         Party_N_N=Random_N['Party'].count()-Party_N_Y

         Party_N=Random_N['Party'].sum()
         if(df.Anti_satellite_test_ban[df.Anti_satellite_test_ban ==1].sum()>0):
           print("")
           print("  Export_south_africa :  " + str(Export_Y_Anti_Y) + " Y  ")
           print("      Party :  " + str(Party_Y_Y) + " Y  ")
           print("      Party :  " + str(Party_Y_N) + " N  ")

           print("  Export_south_africa :  " +str(Export_N_Anti_Y)+ " N")

           print("      Party :  " + str(Party_N_Y) + " Y  ")
           print("      Party :  " + str(Party_N_N) + " N  ")
           # count_y=0;
           # for a in Export_Y_Anti_Y:
           #     if (df.Party[df.Party[a]]==1):
           #         count_y=count_y+1
         #print(df.Party[df.Party])
         print("")

         print("Anti_satellite_test_ban :  " + str(Anti_N) + " N")
         Randm = df[df.Anti_satellite_test_ban == 0]
         Randm_N = (Randm[Randm['Export_south_africa'] == 0])
         Randm_Y = (Randm[Randm['Export_south_africa'] == 1])
         Prty_Y_Y = Randm_Y['Party'].sum()
         Prty_Y_N = Randm_Y['Party'].count() - Party_Y_Y
         Prty_N_Y = Randm_N['Party'].sum()
         Prty_N_N = Randm_N['Party'].count() - Party_N_Y

         print("")

         print("")
         print("  Export_south_africa :  " + str(Export_Y_Anti_N) + " Y  ")
         print("      Party :  " + str(Prty_Y_Y) + " Y  ")
         print("      Party :  " + str(Prty_Y_N) + " N  ")

         print("  Export_south_africa :  " + str(Export_N_Anti_N) + " N")

         print("      Party :  " + str(Prty_N_Y) + " Y  ")
         print("      Party :  " + str(Prty_N_N) + " N  ")
    else:
         Export_Y=df.Export_south_africa[df.Export_south_africa == 1].sum()
         Export_N=df.Anti_satellite_test_ban[df.Anti_satellite_test_ban == 1].count()

         Anti_Y_Export_Y=(df.Anti_satellite_test_ban[df.Export_south_africa ==1]==1).sum()
         Anti_N_Export_Y=(df.Anti_satellite_test_ban[df.Export_south_africa ==1]==0).sum()
         Anti_Y_Export_N = (df.Anti_satellite_test_ban[df.Export_south_africa == 0] == 1).sum()
         Anti_N_Export_N = (df.Anti_satellite_test_ban[df.Export_south_africa == 0] == 0).sum()

         print("Export_south_africa :  " + str(Export_Y) + " Y")

         if(df.Anti_satellite_test_ban[df.Anti_satellite_test_ban ==1].sum()>0):
           print("  Anti_satellite_test_ban :  " + str(Anti_Y_Export_Y) + " Y  AND " +str(Anti_Y_Export_N)+ " N")

         print("Export_south_africa : " + str(Export_N) + " N")
         print("  Anti_satellite_test_ban :  " + str(Anti_N_Export_Y) + " Y  AND " + str(Anti_N_Export_N) + " N")

makeDecisionTree(bestAttribute)
