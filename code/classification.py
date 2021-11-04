# Python ≥3.5 is required
import sys
import numpy as np

# Scikit-Learn ≥0.20 is required
import sklearn
import tensorflow as tf
import tensorflow.python.keras.backend as K
sess = K.get_session()

# Common imports
import numpy as np
import os
import pandas as pd

# To plot pretty figures
import matplotlib as mpl
import matplotlib.pyplot as plt

df1 = pd.read_csv(r'/Users/aopple/COVID_policy_imact_dataset/VA_flow_with_policy.csv')
# print(df1.head(10))
# print(df1.shape)
# print(df1.isna().sum())

from sklearn.model_selection import train_test_split
x = df1[['geoid_o', 'geoid_d', 'date_range', 'visitor_flows', 'pop_flows', 'policy_type']]
y = df1['policy']
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=1)

from sklearn.feature_extraction.text import CountVectorizer

# transform the string to computable data in 'policy_type'
cv = CountVectorizer()
# Use Fit_transform function to compute the parameters and then do the transformation
x_train = cv.fit_transform(x_train['policy_type'])
# Note that we use transform here because we want to use the same paramters learned from training data
x_test = cv.transform(x_test['policy_type'])

# RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier

rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
rf_clf.fit(x_train, y_train)
rf_clf.predict(x_train)
print(rf_clf.predict(x_train))


# Build network using Sequential Model

# Create function returning a compiled network
def create_network():
    # Start neural network
    network = keras.models.Sequential()

    # Add fully connected layer with a ReLU activation function
    network.add(keras.layers.Dense(units=16, activation='relu', input_shape=[7739]))

    # Add fully connected layer with a ReLU activation function
    network.add(keras.layers.Dense(units=16, activation='relu'))

    # Add fully connected layer with a sigmoid activation function
    network.add(keras.layers.Dense(units=1, activation='sigmoid'))

    # Compile neural network
    network.compile(loss='binary_crossentropy',  # Cross-entropy
                    optimizer='sgd',
                    metrics=['accuracy'])  # Accuracy performance metric

    # Return compiled network
    return network


from keras.wrappers.scikit_learn import KerasClassifier

# Wrap Keras model so it can be used by scikit-learn
neural_network = KerasClassifier(build_fn=create_network,
                                 epochs=50,
                                 batch_size=100,
                                 verbose=1)

# # train set / target
# Y_train = tf.keras.utils.to_categorical(Y_train , num_classes=10)
neural_network.fit(x_train, y_train)
