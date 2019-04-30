import requests
import json
import re
from bs4 import BeautifulSoup
from pprint import pprint

filename = "Lecture Video Links.txt.txt"
with open(filename,"r") as f:
    lines = f.readlines()
    #print(lines)
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
lines[0] = "https://www.coursera.org/lecture/text-retrieval/lesson-1-1-natural-language-content-analysis-rLpwp"
#print(len(lines))
# 47,62 are in a different language
#https://www.coursera.org/lecture/text-mining/1-5-text-representation-part-1-6T38K
#https://www.coursera.org/lecture/text-mining/3-2-probabilistic-topic-models-mixture-model-estimation-part-1-QnGYn
# 87 has weird apostrophe problem
#https://www.coursera.org/lecture/text-mining/6-1-opinion-mining-and-sentiment-analysis-latent-aspect-rating-analysis-part-1-dkntE
for i in range(len(lines)):
    print(i)
    if i in [47,62,87]:
        continue
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
    #for j in range(len(data_text)):
        #data_tuples.append((timestamps_text[j],data_text[j]))

    with open("data_text1.txt","a") as f:
        for j in range(len(data_text)):
            #pprint(data_text[j])
            #pprint(lines[87])
            f.write(timestamps_text[j] + ":" + data_text[j] + "\n")

#print(data_text[0])