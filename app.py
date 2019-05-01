from pprint import pprint
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors
import numpy as np
import matplotlib.pyplot as plt

###############################################################################
#
# App:
#   Back-end of the application. Performs the pre-processing, document
#   representation, stop word removal/normalization, and search functions.
#   To change representation, the bag-of-words unigram model, KNN, and stop
#   word removal thresholds can be modified.
#
###############################################################################

# Clean link data for usage, strip ending char
filename = "Lecture Video Links.txt"
with open(filename,"r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
lines[0] = "https://www.coursera.org/lecture/text-retrieval/lesson-1-1-natural-language-content-analysis-rLpwp"

# Pre-process transcript data into text, video #, timestamp
data_tuples = []
data_text = []
lecture_video = -1
with open("data_text.txt","r") as f:
  file = f.readlines()
  for i in range(len(file)):
      split_text = file[i].split(":",2) # delimit format
      timestamp = ":".join(split_text[:2])
      if timestamp == "0:00":
          lecture_video += 1 # indexing for future reference
      text = split_text[2].replace(" \n", "").lower()
      data_text.append(text)
      data_tuples.append((lines[lecture_video],timestamp,text))

# Search function for direct term match
def search(term):
    term = term.lower()
    found_tuples = []
    for i in range(len(data_tuples)):
        if data_tuples[i][2].find(term) != -1:
            found_tuples.append(data_tuples[i])
    return found_tuples

# Build bag-of-words-model with a chosen max df (~0.3 works well) to remove stop words,
# then create feature vectors from data, and build a dictionary to allow O(1) lookup during KNN
vectorizer = CountVectorizer(max_df = 0.3)
feature_vectors = vectorizer.fit_transform(data_text).todense()
vocab_dic = vectorizer.vocabulary_

# Determine frequencies for stop word removal heuristics
sums = np.sum(feature_vectors, axis=0)
sorted_word_frequency = -np.sort(-sums)
sorted_word_frequency = np.asarray(sorted_word_frequency[0]).flatten()

# (Optional) Use pyplot to see removal effect of stop words
plt.xlabel("Word Rank")
plt.ylabel("Word Counts")
plt.title("Word Count vs Work Rank")
plt.plot(range(len(sorted_word_frequency)), sorted_word_frequency, linestyle="", marker="o")

# Used to search a term or phrase; main function
def search_query(term, num_results):
  query = [term]
  query_vector = vectorizer.transform(query)

  # Use KNN with cosine similarity metric, and user-designated k
  neigh = NearestNeighbors(metric="cosine")
  neigh.fit(feature_vectors)
  result = neigh.kneighbors(query_vector, n_neighbors=num_results)
  results = []
  for i in range(num_results):
    # If no results, alert user; if only less than expected, terminate early
    if i == 0 and result[0][0][0] == 1:
      print("Sorry your search query was not found!")
      return results
    if result[0][0][i] == 1:
      return results
    else:
      results.append(data_tuples[result[1][0][i]])
  return results
