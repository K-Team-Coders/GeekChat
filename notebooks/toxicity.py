from detoxify import Detoxify

detoxify_model = Detoxify('multilingual')
alpha = 0.5

def toxicityAnalisis(text):
    results = detoxify_model.predict(text)
    if results["toxicity"] > alpha:
        return 1
    else:
        return 0
        
# pip install detoxify
# 1  ==  токсично
# 0  == не токс
