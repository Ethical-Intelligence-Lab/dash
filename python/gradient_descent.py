import json
import sys
import six
import matplotlib.pyplot as plt

sys.modules['sklearn.externals.six'] = six
import mlrose
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, KBinsDiscretizer
import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score


data_template = load_iris()

with open(f"annotations_weights.json") as f:
    raw_data = json.load(f)

class data():
    def __init__(self):
        self.target = np.array([[annotation['score']] for annotation in raw_data.values()])
        self.data =np.array([list(annotation['weights'].values()) for annotation in raw_data.values()])
data = data()
# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target,
                                                    test_size = 0.2, random_state = 3)

# Normalize feature data
scaler = MinMaxScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# One hot encode target values
bin_encoder = KBinsDiscretizer(n_bins=10, encode='onehot-dense', strategy='uniform')

y_train_binned = bin_encoder.fit_transform(y_train)
y_test_binned = bin_encoder.transform(y_test)

# Initialize neural network object and fit object
nn_model1 = mlrose.NeuralNetwork(hidden_nodes=[], algorithm = 'gradient_descent', curve=True, max_iters = 1000,
                                 bias = True, learning_rate = 0.1,
                                 early_stopping = True, max_attempts = 100,
                                 random_state = 3)

nn_model1.fit(X_train_scaled, y_train_binned)

# Predict labels for train set and assess accuracy
y_train_pred = nn_model1.predict(X_train_scaled)

y_train_accuracy = accuracy_score(y_train_binned, y_train_pred )

print(y_train_accuracy)

# Predict labels for test set and assess accuracy
y_test_pred = nn_model1.predict(X_test_scaled)

y_test_accuracy = accuracy_score(y_test_binned, y_test_pred)

print(y_test_accuracy)