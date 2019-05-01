# 410_Final_Project
CS410 Final Project
Our project serves to aid students who are in CS410 in navigating course videos. 

By using the transcripts as pseudo-documents, we allow students to query in order to find the top k results, their timestamps, their videos, and nearby text. 

This should help students learn and study material more efficiently by allowing them to target content encoded in text, and find associated non-text (video) resources.

Our representation of the text is such that each excerpt from a video (timestamped) is a pseudo-document, and we choose to represent the contents of each of these pseudo-documents with a bag-of-words model. 

To perform the search and ranking, we use k-nearest neighbors via the sklearn package. 

The visual interface is simple, and allows the user to specify k and their query of choice.

The code itself contains the necessary comments and documentation of the implementation for future use, extension, and improvement, and should be referred to. 

To run the code, run app_ui.py in the project directory to bring up the GUI. 

The main libraries and packages we used (and you will need) were:

**Sklearn**: for bag-of-words model, tokenization, and nearest-neighbors

**Numpy**: for array representation and operations

**Tkinter**: for visual interface and UI

**BeautifulSoup & json**: for scraping of site, links, transcripts

**MatPlotLib & pprint**: for console debugging and data pre-process heuristics (optional)

The contributions from each group member to the project were as follows:

Andy: setup, progress videos, search function

Bryant: setup, coordination, progress report, documentation.

Devyn: web scraping, search function

Jasmine: project planning, UI code

Ross: setup, progress report, video
