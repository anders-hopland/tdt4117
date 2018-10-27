import string
from nltk.stem.porter import PorterStemmer
import gensim

class Helper():
    def __init__(self):
        self.translator = str.maketrans('', '', string.punctuation+"\n\r\t")
        self.stemmer = PorterStemmer()
        self.dictionary = gensim.corpora.Dictionary()


    def split_to_paragraphs(self, text):
        return text.split('\r\n\r\n') # Split into seperate paragraphs


    def remove_containing_word(self, list, word):
        return [p for p in list if word not in p] 


    def split_to_words(self, paragraphs):
        for i, p in enumerate(paragraphs):
            paragraphs[i] = p.split(" ")

        return paragraphs


    def remove_punctuations_1d(self, words):
        print("Before func", words)
        for i, word in enumerate(words):
            words[i] = word.lower().translate(self.translator)

        print("Before func", words)
        return words


    def remove_punctuations_2d(self, paragraphs):
        for i, paragraph in enumerate(paragraphs):
            for j, word in enumerate(paragraph):
                paragraphs[i][j] = word.lower().translate(self.translator)

        return paragraphs


    def stem_1d_list(self, words):
        print(words)
        for i, word in enumerate(words):
            words[i] = self.stemmer.stem(word)

        return words


    def stem_2d_list(self, paragraphs):
        for i, paragraph in enumerate(paragraphs):
            for j, word in enumerate(paragraph):
                paragraphs[i][j] = self.stemmer.stem(word)

        return paragraphs


    def get_stopwords(self):
        f = open("stopwords.txt")
        stopwords = f.read()
        stopwords = stopwords.split(",")
        return stopwords


    def get_stopword_ids(self, dictionary):
        stop_words = self.get_stopwords()
        
        stop_word_ids = []
        for s in stop_words:
            try:
                stop_word_ids.append(dictionary.token2id[s])
            except:
                pass

        return stop_word_ids


    def get_bag_of_words(self, words, dictionary):
        bag = []
        for w in words:
            bag.append(dictionary.doc2bow(w))

        return bag

