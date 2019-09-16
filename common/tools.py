import numpy as np

def cal_accuracy_r(model,X_test,y_test):
    
    y_predict = model.predict(X_test)
    y_test = np.array(y_test)

    #　Accuracy rate
    correct_cnt = 0
    for i in range(0,len(y_test)):
        if (y_test[i] - y_predict[i]) == 0:
            correct_cnt +=1

    acc_r = round( correct_cnt  / len(y_test),2)
    return acc_r
