import torch
from transformers import BertTokenizerFast, BertForSequenceClassification

device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Как вариант через  model_path
# !!!
# from pathlib import Path
# model_path = Path.cwd().joinpath("tiny_ready")

tokenizer = BertTokenizerFast.from_pretrained(
    # Путь до папки с tiny_ready
)
model = BertForSequenceClassification.from_pretrained(
    # путь до папки с tiny_ready
    num_labels=2
).to(device)

def get_prediction(text):
    # prepare our text into tokenized sequence
    inputs = tokenizer(text, padding=True, truncation=True, max_length=300, return_tensors="pt").to(device)
    # perform inference to our model
    outputs = model(**inputs)
    # get output probabilities by doing softmax
    probs = outputs[0].softmax(1)
    # executing argmax function to get the candidate label
    labels = {'Нейтральное' : 0, 'Проблемы на линии': 1}

    classes = [0, 1]

    prediction = classes[probs.argmax()]
    text_pred = list(labels.keys())[list(labels.values()).index(prediction)]
    return text_pred