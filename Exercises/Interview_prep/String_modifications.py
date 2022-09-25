from collections import Counter
import string
import re

def top_3_words_1(text):
    result = text.translate(str.maketrans('', '', string.punctuation))
    return result.split()

def top_3_words_2(text):
    words = re.sub(r"[^\w\s\d'-]+", "", text).lower()
    words = words.split()
    word_count = Counter(words)
    most_common = word_count.most_common(3)
    return [most_common[i][0] for i in range(3)]
    # sorted_word_count = {k: v for k, v in sorted(word_count.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)}


def main():
    text = """In a v'illage of La Mancha, the name of which I have no desire to call
    to mind, there lived not l'ong since one of those gentlemen that keep a lance
    in the lance-rack, an old buckler, a lean hack, and a greyhound for
    coursing. An olla of rather more beef than mutton, a salad on most
    nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
    on Sundays, made away with three-quarters of his income."""

    # print(top_3_words_1(text), "\n")
    words = top_3_words_2(text)
    print(words)


if __name__ == "__main__":
    main()