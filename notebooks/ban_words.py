from pathlib import Path

ban_words_txt_path = Path().cwd().joinpath("censor.txt")

words = ""
with open(ban_words_txt_path, "r", encoding="utf-8") as f:
    words = f.read()

words = words.split("\n")


def containsBanWords(text):
    if text in words:
        return 1
    else:
        return 0
