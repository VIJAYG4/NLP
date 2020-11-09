import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

sentences = sent_tokenize("That is a beautiful orange flower.")
words = word_tokenize("Fish sleep.")

for i, sentence in enumerate(sentences):
    print(f'Sentence {i}: {sentence}')
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)
    for word, tag in tags:
        print(f'{word}: {tag}')
    print()
