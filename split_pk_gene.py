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
        
    return data_train,label_train,data_test,label_test