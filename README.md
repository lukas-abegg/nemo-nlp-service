# nemo-nlp-service
This service shows prototypical different nlp services which can improve the reading and searching behaviour of our customers on the platforms. The idea of this service is to help understanding the difference between the different approaches and how they can be applied and positively impact the user experience on our platforms.

We have implemented the following services:
 * General Text Tagger
 * Medical Text Tagger
 * Text Summarizer
 * Text Similarity Calculator

##  General Text Tagger
This tagger recognizes entities like persons, groups, organisations, etc. and is made for general text like news articles or wikipedia.

## Medical Text Tagger
This tagger recognizes medical terms and entities and is able to distinguish between diseases in English.

It also performs linking of an entity to the Unified Medical Language System (UMLS) entries. 

## Text Summarizer
This service summarizes your text into a compact abstract or summary respectively. You can compare different libraries with each other and their summarizing qualities.

The used models are for text in English. Models for text in German are also available. 

## Text Similarity Calculator
This text comparison can be used to find similarities in text.

You can imagine this function to work similar to a search. It calculate the relevance of one text for another text (i.e., one text is the query, the other one the found document with a certain relevance). 

## Setup und Running of the Service

### 1. Installation
   * you need python 3.7
   * for installation of required python packages run:
```bash
$ pip install -r requirements
```
### 2. Run Server
   * To run the server you just need to run
```bash
$ python -m flask run
```
### 3. Open Webapp
   * Server runs on port 5000
   * Type into your browser

Go to: http://127.0.0.1:5000
