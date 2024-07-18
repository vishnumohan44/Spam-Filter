# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

from sklearn import preprocessing 
from sklearn.preprocessing import RobustScaler
from sklearn.metrics import mean_squared_error

def spam_predict(msg):
    df = pd.read_csv("spam.csv", encoding='latin1')
    df.head()

    # Removing the unwanted columns generated as a result of encoding
    df.drop(columns=['Unnamed: 2', 'Unnamed: 3', "Unnamed: 4"], inplace=True)

    # Renaming the column 'v1' to 'category' and 'v2' to 'message'
    df.rename(columns = {'v1':'Category'}, inplace = True)
    df.rename(columns = {'v2':'Message'}, inplace = True)
    df.head()

    # Inspecting the data
    df.groupby('Category').describe()

    # Encoding 'category' according to spam or not spam.
    # 1 if spam, 0 if not
    df['spam'] = df['Category'].apply(lambda x:1 if x=='spam' else 0)
    df.head()

    # Splitting the data into train and test
    x = df.Message
    y = df.spam
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    x_train.describe(), x_test.describe()

    y_train.describe(), y_test.describe()

    # Counting the frequecy of each word using the count vectorizer
    # Finding the word count and storing the data as a numerical matrix
    count = CountVectorizer()
    x_train_count = count.fit_transform(x_train.values)
    x_train_count.toarray()

    # Declaring and fitting our data to the naive bayes model
    classifier = MultinomialNB()
    classifier.fit(x_train_count, y_train)

    # Pretest
    email_ham = ["You won 1000$. Click the link below"]
    email_ham_count = count.transform(email_ham)
    classifier.predict(email_ham_count)

    # Count vectorizing the test dataset
    x_test_count = count.transform(x_test)
    # Testing the accuracy
    classifier.score(x_test_count, y_test)*100

    # user_message = input()
    inp = [msg]
    message_count = count.transform(inp)
    return classifier.predict(message_count)
