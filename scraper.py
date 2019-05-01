import requests
import json
import re
from bs4 import BeautifulSoup
from pprint import pprint

###############################################################################
#
# Scraper:
#   Scrapes the course website for associated transcripts and text data, and
#   stores them in a dump file. Note that scraping url(s) and links are subject
#   to change and should be updated accordingly should they change.
#
###############################################################################

# Clean link data for usage, strip ending char
filename = "Lecture Video Links.txt"
with open(filename,"r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
lines[0] = "https://www.coursera.org/lecture/text-retrieval/lesson-1-1-natural-language-content-analysis-rLpwp"

# *Below are some nuances with the scraping, and some associated problems
# 47,62 are in a different language
# https://www.coursera.org/lecture/text-mining/1-5-text-representation-part-1-6T38K
# https://www.coursera.org/lecture/text-mining/3-2-probabilistic-topic-models-mixture-model-estimation-part-1-QnGYn
# 87 has weird apostrophe problem
# https://www.coursera.org/lecture/text-mining/6-1-opinion-mining-and-sentiment-analysis-latent-aspect-rating-analysis-part-1-dkntE
for i in range(len(lines)):
    print(i)
    if i in [47,62,87]:  # Deals with the aforementioned
        continue

    # Parse text data, timestamps, via pattern matching
    url = lines[i]
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    data = soup.find_all('div', {"class" : "phrases"})

    timestamps = soup.find_all('button',{"class" : "timestamp"})
    timestamps_text = []
    for time in timestamps:
        timestamps_text.append(time.text)

    data_text = []
    for elem in data:
        data_text.append(elem.text)
    data_tuples = []

    # Write out results to dump file; call this to **overwrite** previous text dump!
    with open("data_text.txt","w") as f:
        for j in range(len(data_text)):
            f.write(timestamps_text[j] + ":" + data_text[j] + "\n")