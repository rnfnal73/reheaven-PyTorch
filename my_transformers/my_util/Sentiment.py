import pickle
import torch
import os

def getSentiment():
    file_path = os.path.dirname(os.path.realpath(__file__))
    weight = []
    senti_list = []
    with open(file_path+'/senti_list.txt','rb') as fd:
        senti_list = pickle.load(fd) # input_ids와 match되는 값
        weight = pickle.load(fd)
    return weight,senti_list