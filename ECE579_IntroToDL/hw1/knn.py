import math
import numpy as np  
from download_mnist import load
import operator  
import time
# classify using kNN  
#x_train = np.load('../x_train.npy')
#y_train = np.load('../y_train.npy')
#x_test = np.load('../x_test.npy')
#y_test = np.load('../y_test.npy')
x_train, y_train, x_test, y_test = load()
x_train = x_train.reshape(60000,28,28)
x_test  = x_test.reshape(10000,28,28)
x_train = x_train.astype(float)
x_test = x_test.astype(float)
def kNNClassify(newInput, dataSet, labels, k): 
    result=[]
    ########################
    # Input your code here #
    ########################

    for oneInput in newInput:
        # calculate the distance between test data to other points
        dists=np.linalg.norm(np.subtract(dataSet,oneInput),axis=(1,2))
        # get the index of the nearest k points
        minis_index=np.argsort(dists)[:k]
        # use the index to get the label of nearest points
        minis_label=[labels[i] for i in minis_index]
        # find the most common label in candidates
        label=np.argmax(np.bincount(minis_label))
        # add one label to result array
        result.append(label)
    
    
    ####################
    # End of your code #
    ####################
    return result

start_time = time.time()
outputlabels=kNNClassify(x_test[10:120],x_train,y_train,10)
result = y_test[10:120] - outputlabels
result = (1 - np.count_nonzero(result)/len(outputlabels))
print ("---classification accuracy for knn on mnist: %s ---" %result)
print ("---execution time: %s seconds ---" % (time.time() - start_time))
