import random; random.seed(123)
import codecs
import re
import gensim
from lib.helpers import Helper

helper = Helper()

f = codecs.open("pg3300.txt", "r", "utf-8")

text = f.read()
paragraphs = helper.split_to_paragraphs(text)
print("Before")
print(len(paragraphs))
paragraphs = helper.remove_containing_word(paragraphs, "Gutenberg".lower()) # Filter out headers and footers
print("After")
print(len(paragraphs))
words = helper.split_to_words(paragraphs[:])
processed_words = helper.remove_punctuations_2d(words)
stemmed_words = helper.stem_2d_list(processed_words)

# Part two
dictionary = gensim.corpora.Dictionary(stemmed_words)
stop_word_ids = helper.get_stopword_ids(dictionary)

dictionary.filter_tokens(stop_word_ids)

bag_of_words = helper.get_bag_of_words(stemmed_words, dictionary)

# Part three
# tf-idf
tfidf_model = gensim.models.TfidfModel(bag_of_words)
tfidf_corpus = tfidf_model[bag_of_words]
similarity_mat_tfidf = gensim.similarities.MatrixSimilarity(tfidf_corpus)

# lsi
lsi_model = gensim.models.LsiModel(tfidf_corpus, id2word=dictionary, num_topics=100)
lsi_corpus = lsi_model[bag_of_words]
similarity_mat_lsi = gensim.similarities.MatrixSimilarity(lsi_corpus)

print(lsi_model.show_topics(3))

# Part four
query = "How taxes influence economics?"
query = query.split(" ")
print(query)
query = helper.remove_punctuations_1d(query)
print(query)
query = helper.stem_1d_list(query)
query = dictionary.doc2bow(query)

tfidf_model_query = tfidf_model[query]

docsim = enumerate(similarity_mat_tfidf[tfidf_model_query])
docs = sorted(docsim, key=lambda kv: -kv[1])[:3]
print(docs)
print(paragraphs[docs[0][0]])
print(paragraphs[docs[1][0]])
print(paragraphs[docs[2][0]])

