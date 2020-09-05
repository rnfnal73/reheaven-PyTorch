import pickle
import torch

def getSentiment():
    weight = []
    senti_list = []
    with open('/gdrive/My Drive/nlp/KoElectra/finetune/src/my_transformers/my_util/senti_list.txt','rb') as fd:
        senti_list = pickle.load(fd) # input_ids와 match되는 값
        weight = pickle.load(fd)
    return weight,senti_list