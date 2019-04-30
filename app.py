from pprint import pprint
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import matplotlib.pyplot as plt

filename = "Lecture Video Links.txt"
with open(filename,"r") as f:
    lines = f.readlines()
    #print(lines)
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
lines[0] = "https://www.coursera.org/lecture/text-retrieval/lesson-1-1-natural-language-content-analysis-rLpwp"
#pprint(lines)

data_tuples = []
data_text = []
lecture_video = -1
with open("data_text.txt","r") as f:
  file = f.readlines()
  for i in range(len(file)):
      split_text = file[i].split(":",2)
      timestamp = ":".join(split_text[:2])
      if timestamp == "0:00":
          lecture_video += 1
      text = split_text[2].replace(" \n", "").lower()
      data_text.append(text)
      data_tuples.append((lines[lecture_video],timestamp,text))
  #pprint(data_tuples[0:60])

def search(term):
    term = term.lower()
    found_tuples = []
    for i in range(len(data_tuples)):
        if data_tuples[i][2].find(term) != -1:
            found_tuples.append(data_tuples[i])
    return found_tuples

pprint(search("clustering"))
pprint(data_text)

# Build bag-of-words-model
vectorizer = CountVectorizer(max_df = 0.3)
feature_vectors = vectorizer.fit_transform(data_text).todense()
#np.set_printoptions(threshold=1000)
vocab_dic = vectorizer.vocabulary_
print(feature_vectors)
print(vocab_dic)

sums = np.sum(feature_vectors, axis=0)
sorted_word_frequency = -np.sort(-sums)
sorted_word_frequency = np.asarray(sorted_word_frequency[0]).flatten()

plt.xlabel("Word Rank")
plt.ylabel("Word Counts")
plt.title("Word Count vs Work Rank")
plt.plot(range(len(sorted_word_frequency)), sorted_word_frequency, linestyle="", marker="o")

# Perform Query
query = ["text retrieval"]
query_vector = vectorizer.transform(query)
num_results = 10

from sklearn.neighbors import NearestNeighbors
neigh = NearestNeighbors(metric="cosine")
neigh.fit(feature_vectors)
result = neigh.kneighbors(query_vector, n_neighbors=num_results)
print(result)
for i in range(num_results):
  if i == 0 and result[0][0][0] == 1:
    print("Sorry your search query was not found!")
    break
  if result[0][0][i] == 1:
    break
  else:
    pprint(data_tuples[result[1][0][i]])