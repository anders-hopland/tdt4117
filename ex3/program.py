import random; random.seed(123)
import codecs
import re
import gensim
from lib.helpers import Helper

helper = Helper() # Helper functions

# Part one

f = codecs.open("pg3300.txt", "r", "utf-8")

text = f.read()
paragraphs = helper.split_to_paragraphs(text)
paragraphs = helper.remove_containing_word(paragraphs, "Gutenberg".lower()) # Filter out headers and footers
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
query = helper.remove_punctuations_1d(query)
query = helper.stem_1d_list(query)
print("Stemmed query: ", query, "\n\n")
query = dictionary.doc2bow(query)

tfidf_model_query = tfidf_model[query]

print("\n\n--- TF-IDF: ---\n\n")

docsim = enumerate(similarity_mat_tfidf[tfidf_model_query])
docs = sorted(docsim, key=lambda kv: -kv[1])[:3]
for i, (p, score) in enumerate(docs):
    print("[paragraph: %d, score: %f]" % (p, score))
    for ln, line in enumerate(paragraphs[p].split('\n')):
        if ln == 5:
            print("...")
            break
        print(line)
    print()


# LSI
print("\n\n--- LSI ---\n\n")

lsi_query = lsi_model[tfidf_model_query]
#print(sorted(lsi_query, key=lambda kv: -abs(kv[1]))[:3])
doc2similarity = enumerate(similarity_mat_lsi[lsi_query])
docs = sorted(doc2similarity, key=lambda kv: -kv[1])[:3]
#print(docs)
for i, (p, score) in enumerate(docs):
    print("[paragraph: %d, score: %f]" % (p, score))
    for ln, line in enumerate(paragraphs[p].split('\n')):
        if ln == 5:
            print("...")
            break
        print(line)
    print()
