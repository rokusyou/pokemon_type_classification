import numpy as np
def split_pk_gene(gene,pk_data,pk_label):
    # test data is first generation
    if gene == 'first': # (RED & GREEN)
        train_num = 150
        data_train  = pk_data[train_num:]
        data_test   = pk_data[:train_num]
        label_train = pk_label[train_num:]
        label_test  = pk_label[:train_num]
    elif gene == 'sm': # SUN & MOON
        train_num = 721
        data_train  = pk_data[:train_num]
        data_test   = pk_data[train_num:]
        label_train = pk_label[:train_num]
        label_test  = pk_label[train_num:]
    else :
        train_num = 721
        data_train  = pk_data[:train_num]
        data_test   = pk_data[train_num:]
        label_train = pk_label[:train_num]
        label_test  = pk_label[train_num:]
    
    data_train = np.array(data_train)
    data_test = np.array(data_test)
    label_train = np.array(label_train)
    label_test  = np.array(label_test)
    
    return data_train,label_train,data_test,label_test