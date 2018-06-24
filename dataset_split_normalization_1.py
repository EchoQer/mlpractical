#dataset split and normalization

import numpy as np
import json
import math

TRAIN_PARTITION = 0.8
VAL_PARTITION = 0.1

data_set = {}
training_data = {}
validation_data = {}
test_data = {}

# =============================================================================

def read_file(path):
    
    with open(path,'r') as load_f:
        load_dict = json.load(load_f)
        print("Load file succeed..." + path)
    return load_dict

# =============================================================================
    
def write_grid_internet_activity(dict_data,file_path):
    with open(file_path,"w") as f:
        json.dump(dict_data,f)
        print("Write file succeed..." + file_path)

# =============================================================================
        
def deta_normalization(data_dic):
    
    data = {}
    temp = list(data_dic.values())
    mean = np.array(temp).mean()
    std = np.array(temp).std()

    for key in data_dic.keys():    
        temp = data_dic[key]
        value = [[(temp[i][j] - mean)/std for j in range(len(temp[i]))] for i in range(len(temp))]

        data[key] = value
    return data

def max_min_normalization(data_dic):
    
    
    data = {}
    temp = list(data_dic.values())

    max_ = np.array(temp).max()
    min_ = np.array(temp).min()

    for key in data_dic.keys():  
        temp = data_dic[key]
        value = [[(temp[i][j] - min_)/(max_ - min_) for j in range(len(temp[i]))] for i in range(len(temp))]
        data[key] = value
    return data

# =============================================================================



for i in range(1,63):
    
    path = 'data/'  + str(i) + '.json'
    if i == 1 :
        dataset = read_file(path)
    else:
        dataset = dict(dataset, **read_file(path))

        
data = deta_normalization(dataset)
length = len(data)

train_size = math.floor( TRAIN_PARTITION * length)
val_size = math.floor( VAL_PARTITION * length)

index = 1
for key in data.keys():
    
    if index in range(1, train_size + 1):
        training_data[key] = data[key]
       
    else:
        if index in range(train_size + 1, train_size + val_size + 1):
            validation_data[key] = data[key]
            
        else:
            test_data[key] = data[key]
            
    index = index + 1           
  
print(len(training_data))    
print(len(validation_data))    
print(len(test_data))    
 
write_grid_internet_activity(training_data,'data/training.json')
write_grid_internet_activity(validation_data,'data/validation.json')
write_grid_internet_activity(test_data,'data/test.json')
 
