from sklearn.metrics import accuracy_score

#accuracy degradation detector
def detector(trainSet, liveSet, parameters):
    firstColumn = liveSet.axes[1][0]
    secondColumn = liveSet.axes[1][1]
    
    accuracy = accuracy_score(liveSet[firstColumn].to_list(), liveSet[secondColumn].to_list())
    threshold = float (parameters.get("threshold", 0.8))
    return int(accuracy < threshold), accuracy