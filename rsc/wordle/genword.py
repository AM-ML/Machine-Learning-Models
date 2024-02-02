import random
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet

synsets = list(wordnet.all_synsets(pos="n"))
def get_random_word():
    words = [lemma.name() for synset in random.sample(synsets, min(len(synsets), 10)) for lemma in synset.lemmas() if 6 >= len(lemma.name()) >= 4]
    if not synsets:
        return None
    return random.choice(words)

def generate_dict_file(file_path, num_words):
    with open(file_path, 'w') as file:
        for _ in range(num_words):
            word = get_random_word()
            if word and "_" not in word:
                file.write(word + '\n')

# Generate dict.txt with 500 words
generate_dict_file('dict.txt', 200)

