# Importing the required libraries

import numpy as np  # Numpy is a library for scientific computing with Python
import pandas as pd # Pandas is a library for data manipulation and analysis
import matplotlib.pyplot as plt # Matplotlib is a plotting library
import nltk # Natural Language Toolkit

# Reading the data
Psy = pd.read_csv('Youtube01-Psy.csv')
Katy = pd.read_csv('Youtube02-KatyPerry.csv')
Eminem = pd.read_csv('Youtube04-Eminem.csv')
Shakira = pd.read_csv('Youtube05-Shakira.csv')
LMFAO = pd.read_csv('Youtube03-LMFAO.csv')


# Concatenate all data into one DataFrame
df = pd.concat([Shakira, Eminem, Katy, Psy, LMFAO])
df.drop('DATE', axis=1, inplace=True)
df.shape

# Duplicates has been checked and removed
df.duplicated()
df.drop_duplicates()

# Printing the first 5 rows of the dataframe
df.head()

# Counted the instances of each class and plotted them
# 1 is spam and 0 is ham (not spam)
df['CLASS'].value_counts().plot(kind='bar')

classes = df['CLASS']
print(classes.value_counts())

text_messages = df["CONTENT"]

# use regular expressions to replace email addresses, URLs, phone numbers, other numbers

# Replace email addresses with 'email'
processed = text_messages.str.replace(r'^.+@[^\.].*\.[a-z]{2,}$',
                                 'emailaddress')

# Replace URLs with 'webaddress'
processed = processed.str.replace(r'^http\://[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(/\S*)?$',
                                  'webaddress')

# Replace money symbols with 'moneysymb' (£ can by typed with ALT key + 156)
processed = processed.str.replace(r'£|\$', 'moneysymb')

# Replace 10 digit phone numbers (formats include paranthesis, spaces, no spaces, dashes) with 'phonenumber'
processed = processed.str.replace(r'^\(?[\d]{3}\)?[\s-]?[\d]{3}[\s-]?[\d]{4}$',
                                  'phonenumbr')

# Replace numbers with 'numbr'
processed = processed.str.replace(r'\d+(\.\d+)?', 'numbr')

print(text_messages[:20])

processed = processed.str.replace(r'[^\w\d\s]', ' ')

# Replace whitespace between terms with a single space
processed = processed.str.replace(r'\s+', ' ')

# Remove leading and trailing whitespace
processed = processed.str.replace(r'^\s+|\s+?$', '')

# change words to lower case - Hello, HELLO, hello are all the same word
processed = processed.str.lower()
print(processed)