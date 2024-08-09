# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 10:56:54 2024

@author: DIVYANSHU
"""


import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import keras
import keras_tuner

# Load the dataset
data = pd.read_csv('/Users/DIVYANSHU/Desktop/Deep Learning/Iris_Detection/Iris - all-numbers.csv') #insert your own model path here

# Extract features (first four columns)
X = data.iloc[:, :4].values

# Extract labels (last column)
y = data.iloc[:, -1].values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Build the model
model = Sequential()
model.add(Dense(128, input_shape=(4,), activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.7))
model.add(Dense(100, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(100, activation='relu'))
model.add(Dense(3, activation='softmax'))  # Output layer with 3 neurons for 3 classes

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=200, batch_size=5, verbose=1)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Accuracy: {accuracy}')

model.save('iris_dt.keras')