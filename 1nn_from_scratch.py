from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np


# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target


# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=40,
    random_state=42
)


# 1-Nearest Neighbor classifier
def predict_1nn(x, X_train, y_train):
    # Calculate Euclidean distance from x to every training point
    dist = np.sqrt(np.sum((X_train - x) ** 2, axis=1))

    # Find the closest training point
    min_index = np.argmin(dist)

    # Return the label of the closest point
    return y_train[min_index]


# Predict all test samples
pred = {}

for i in range(len(X_test)):
    pred[i] = predict_1nn(X_test[i], X_train, y_train)


# Display predictions
print("Predicted:", pred)
print("Actual:", y_test)


# Calculate accuracy
correct = 0

for i in range(len(X_test)):
    if pred[i] == y_test[i]:
        correct += 1

accuracy = correct / len(X_test)

print("Accuracy:", accuracy)
