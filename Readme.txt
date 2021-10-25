CZ4045 Natural Language Processing - Assignment 1

Introduction

This README provides instructions for installation methods for third party libraries. The objective of the assignment is to understand the main components in a NLP application. At the same time analyse the
limitations that are faced when implementing an NLP concept.

File Structure

The main folders are split into three categories 'data', 'result' and 'src'.

data : The data folder contains all the datasets required for the codes.

   • reviewSelected100.json
   • cnaOne.docx
   • cnaTwo.docx

result : The result folder contains the respective csv files obtained for 'Application', 'Extraction', and 'Noun-Adjective Pair'.

src : The src folder contains all the base codes for the assignment. All files are labelled according to their respective headings as specified in the report.

Installation manual

   • Python libraries are installed in the respective .ipynb files.
   • For Questions 1.2, 1.3, 1.4, 1.5 and 3 only python libraries are required.
   • For 2. Extraction of indicative adjective phrase.ipynb a stanford core server is required to run in the background. Please refer to Stanford Core Server Setup.

Dependencies

  1. VADER - Sentiment Analysis Tool provided by NLTK
  2. Natural Language Toolkit
  3. spaCy
  4. pandas
  5. Natural Language Toolkit
  6. BeautifulSoup
  7. numpy
  8. requests
  9. docx2text
 10. language_tool_python
 11. CNA Post Documents

Stanford Core Server Setup

1. Download and install stanford core NLP

  1. Please visit StanfordCore to download stanford core nlp
  2. Unzip the downloaded file
  3. Download and install Java

   • For Windows 
   • For macOS 
   • For Linux 

2. Run background server

  1. Open a terminal at the directory of stanford core nlp file
  2. Run the following command in terminal

java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -preload tokenize,ssplit,pos,lemma,ner,parse,depparse -status_port 9000 -port 9000 -timeout 100000000000000000000000 &
On a successful connection to the server, the message below is shown 
[main] INFO CoreNLP - StanfordCoreNLPServer listening at /0:0:0:0:0:0:0:0:9000 

  3. Upon receiving the output shown above, the 2. Extraction of indicative adjective phrase.ipynb can be run.

Sample Results for Question 3.4 Application

Model Results

Depending on the accuracy of the sentiment analysis tool (VADER), there are some cases where the label of the review was incorrect in comparison to an actual label that can be determined based on
contextual knowledge. Due to this limitation, model accuracy during training is decreased forming instances of invalid predictions. However, there are also cases where the model successfully identifies the
valid label although the actual label assigned by VADER is wrong.
