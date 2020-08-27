import sys
#print(sys.path)
import torch
from my_transformers import(
    ElectraConfig,
    ElectraForSequenceClassification,
    ElectraTokenizer,
)

labels = ["0", "1"]

config = ElectraConfig.from_pretrained(
            "monologg/koelectra-small-discriminator",
            num_labels=2,
            id2label={str(i): label for i, label in enumerate(labels)},
            label2id={label: i for i, label in enumerate(labels)},
        )
model = ElectraForSequenceClassification(config)
#print('my model',model)
loaded = torch.load("C:\jupyter_notebook/koelectra-small-nsmc-ckpt_rnn_gpu/checkpoint-2000/pytorch_model.bin",map_location='cpu')  #torch.load(PATH,map_location), map_location은 model을 load하는 device 종류
#print('loaded',loaded)
model.load_state_dict(loaded,strict=False)
#print(model)

tokenizer = ElectraTokenizer.from_pretrained("monologg/koelectra-base-discriminator")

sentence = '나이스 !!!!!'

tokenized_sentence= tokenizer.tokenize(sentence)

#print('generated tokens: ',tokenized_sentence)

gen_encoded = tokenizer.encode(tokenized_sentence, return_tensors="pt") # model내 vocabulary에 있는 id로 토큰을 mapping(encoding)


model_input = gen_encoded

classification_result = model(model_input)
result = torch.argmax(classification_result[0][0])
if result.item() == 1:
	result = '긍정'
else:
	result = '부정'
print('input sentence: ',sentence ,'=',result)