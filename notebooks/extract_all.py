from notebooks.sentiment import get_sentiment
from notebooks.toxicity import toxicityAnalisis
from notebooks.troubles_tiny import get_prediction
from notebooks.ban_words import containsBanWords


def extractFullTextData(text):
    sentiment_res = get_sentiment(text)
    toxicity_res = toxicityAnalisis(text)
    troubles_res = get_prediction(text)
    ban_res = containsBanWords(text, True)

    modded_text = None

    if toxicity_res == 0:
        toxicity_res = "Не токсичный"
    else:
        toxicity_res = "Токсичный"

    if ban_res[0] == 0:
        ban_res = "Не содержит обсценной лексики"
    else:
        bad_word = ban_res[1]
        ban_res = "Содержит обсценную лексику"
        modded_text = text.replace(bad_word, "*" * len(bad_word))

    if troubles_res == 1:
        troubles_res = "В сессии есть технические проблемы"
    else:
        troubles_res = "Технических проблем не обнаружено"

    if modded_text:
        text = modded_text

    if sentiment_res == "negative":
        sentiment_res = "Негативное настроение"
    elif sentiment_res == "positive":
        sentiment_res = "Позитивное настроение"
    else:
        sentiment_res = "Нейтральное настроение"

    common_result = {
        "text": text,
        "toxicity": toxicity_res,
        "sentiment": sentiment_res,
        "troubles": troubles_res,
        "ban": ban_res
    }

    return common_result
