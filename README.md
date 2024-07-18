# Spam-Filter
A mini-project to identify spam messages using a Multinomial Naive Bayes Model.

Run only "main.py" file. Make sure all the files are in the same folder before running.

```
Libraries:
1. Pandas: For data manipulation and analysis.
2. NumPy: For numerical operations.
3. Seaborn & Matplotlib: For data visualization (though not used in this snippet).
4. Scikit-Learn: For machine learning algorithms and tools.
```

This project implements a spam detection system using the Multinomial Naive Bayes model, which is a probabilistic classifier particularly suited for text classification tasks. Initially, various essential libraries for data manipulation, visualization, and machine learning are imported. The dataset spam.csv is then loaded into a DataFrame, where unnecessary columns are removed, and the remaining columns are renamed for clarity. The 'Category' column, which indicates whether a message is spam or not, is encoded into numerical values: 1 for spam and 0 for not spam. The data is subsequently split into training and testing sets to allow for model evaluation.

The CountVectorizer is employed to convert the text messages into a numerical matrix of token counts, enabling the model to process the text data. A Multinomial Naive Bayes classifier is then initialized and trained on the training data. After training, the model's accuracy is evaluated using the test data to ensure its effectiveness. Finally, the system is capable of predicting whether a new, unseen message is spam or not by vectorizing the input message and using the trained model to classify it accordingly. This approach leverages the frequency of words in the messages to determine the likelihood of a message being spam, making it a practical solution for text-based spam detection.
