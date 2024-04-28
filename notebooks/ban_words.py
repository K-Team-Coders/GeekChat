from pathlib import Path

ban_words_txt_path = Path().cwd().joinpath("./notebooks/censor.txt")

words = ""
with open(ban_words_txt_path, "r", encoding="utf-8") as f:
    words = f.read()

words = words.split("\n")


def containsBanWords(text, return_what = False):
    clean = True
    bad_word = ""
    for word in text.split():
        if word in words:
            clean = False
            bad_word = word

    if clean:
        if return_what:
            return 0, None
        else:
            return 0
    else:
        if return_what:
            return 1, bad_word
        else:
            return 1
