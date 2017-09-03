# Perceptron-Binary-Text-Classifier
A binary Text Classifier for spam Filtering of emails with tokenized data using the Perceptron - a machine learning model for supervised learning.

Classification technique: Perceptron

- This model uses  the perceptron model to classify if a particular email is ham or spam. Requires tokenized emails to create a model for classification. It builds a vocabulary of the distinct words (tokens) from email data and calculates their respective weights. Dump the data in the model file to be used later to classift random data.
Dataset required:

For perlearn.py:

Tokenized data files of emails pre classified as ham ( valid ) and spam ( invalid ) emails in their respective folders i.e "ham" or "spam" in lowercase.

For perclassify.py:

Tokenized data files from emails.

Instructions to Run:

Step 1) Objective: Creating a classification model to be used as a reference for future use by learning from the tokenized dataset.

  Program file: nblearn.py

  Input: It takes command line input that is a directory path to tokenized data For eg) C:\Users\XYX\Desktop\data_folder

  Output: Model file

    You can find the sample model file generated previously for a dataset named as nbmodel.txt

Step 2)

  Objective: Classifying the random data using the model file generated in step 1.

  Program file: nbclassify.py / avg_perclassify.py

  Input: 1) permodel.txt file 2) Random tokenized data file.

  Output: the efficiency of the program for eg) 99/100
