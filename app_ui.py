import tkinter
from tkinter import *

###########################################
from pprint import pprint
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors
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

# Build bag-of-words-model
vectorizer = CountVectorizer(max_df = 0.3)
feature_vectors = vectorizer.fit_transform(data_text).todense()
vocab_dic = vectorizer.vocabulary_

sums = np.sum(feature_vectors, axis=0)
sorted_word_frequency = -np.sort(-sums)
sorted_word_frequency = np.asarray(sorted_word_frequency[0]).flatten()

plt.xlabel("Word Rank")
plt.ylabel("Word Counts")
plt.title("Word Count vs Work Rank")
plt.plot(range(len(sorted_word_frequency)), sorted_word_frequency, linestyle="", marker="o")

# Used to search a term or phrase
def search_query(term, num_results):
  query = [term]
  query_vector = vectorizer.transform(query)

  neigh = NearestNeighbors(metric="cosine")
  neigh.fit(feature_vectors)
  result = neigh.kneighbors(query_vector, n_neighbors=num_results)
  results = []
  for i in range(num_results):
    if i == 0 and result[0][0][0] == 1:
      print("Sorry your search query was not found!")
      return results
    if result[0][0][i] == 1:
      return results
    else:
      results.append(data_tuples[result[1][0][i]])
  return results
#pprint(search_query("text retrieval", 5))




###############################################

def get_tuples():

 	#would perform the search here
    links = ["<put links here>", "https://www.coursera.org/learn/text-mining/lecture/8Ki0H/4-4-text-clustering-generative-probabilistic-models-part-3"]
    text = ["<text results go here>", "and what the likelihood function looks like. And we can also compute the maximum likelihood estimate, to estimate the parameters. In this lecture, we're going to do talk more about how exactly we're going to compute the maximum likelihood estimate. As in most cases the Algorithm can be used to solve this problem for mixture models. So here's the detail of this Algorithm for document clustering. Now, if you have understood how Algorithm works for topic models like TRSA, and I think here it would be very similar. And we just need to adapt a little bit to this new mixture model. So as you may recall Algorithm starts with initialization of all the parameters. So this is the same as what happened before for topic models."]

    results = []
    for i in range(len(links)):
    	results.append((links[i], text[i]))

    return results

#clicking submit button triggers this function
def submit():

    #we can get the users keywords they entered like this:
    user_input = search_box.get()
    num_results = int(v.get())

    result = search_query(user_input, num_results)

    #return results:
    Label(root, text="Results:").grid(row=2)

    prev = 4 #start at grid row 4
    for tup in result:
        Label(root, text=tup[0], fg="blue").grid(row=prev, column=1,pady=(25,0))
        prev = prev+4
        result = Text(root, height=4, width=100)
        result.insert(INSERT, tup[2])
        result.grid(row=prev, column=1)
        Label(root, text=tup[1]).grid(row=prev, column=0)
        prev= prev + 4



if __name__ == '__main__':

    # this is the main window frame to build off of
    root = tkinter.Tk()

    #add search / text entry box to take in user inputs
    Label(root, text="Search Keywords:", fg="blue").grid(row=0)
    search_box = Entry(root, bd=5)
    search_box.grid(row=0, column=1)
    Button(root, command=submit, text="Submit").grid(row=0, column=3)

    ##option meaning
    my_options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    v = StringVar()
    v.set("5")
    om = OptionMenu(root, v, *my_options)
    om.grid(row=0, column=2)

    root.mainloop()
