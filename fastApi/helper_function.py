import asyncio
from loguru import logger

from notebooks.sentiment import *


def score_calculate_emotion_coloring(comment):
    result = get_sentiment(comment, 'label')
    if result == 'neutral':
        return 0
    elif result == 'positive':
        return 1
    elif result == 'negative':
        return -1


async def update_activity(comment_counter, num_users):
    while True:
        await asyncio.sleep(600)  # 600 секунд = 10 минут
        # Рассчитаем активность
        activity = (comment_counter / num_users) / 10 * 100
        logger.info(f"Activity: {activity}")
