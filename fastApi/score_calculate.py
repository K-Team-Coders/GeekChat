from notebooks.sentiment import *


def score_calculate_emotion_coloring(comment):
    result = get_sentiment(comment, 'label')
    if result == 'neutral':
        return 0
    elif result == 'positive':
        return 1
    elif result == 'negative':
        return -1
