# 1-Nearest Neighbor from Scratch

A simple implementation of the **1-Nearest Neighbor (1-NN)** classification algorithm using the Iris dataset.

The goal of this exercise is to understand how KNN works internally rather than using `sklearn.neighbors.KNeighborsClassifier`.

## Concepts

- Train/Test Split
- Euclidean Distance
- Nearest Neighbor
- NumPy vectorized operations
- Classification
- Accuracy

## How 1-NN Works

For every test sample:

1. Calculate its Euclidean distance from every training sample.
2. Find the training sample with the smallest distance.
3. Take the label of that nearest training sample.
4. Use that label as the prediction.

### Euclidean Distance

$$
d(x,a) = \sqrt{\sum_i (x_i-a_i)^2}
$$

## Dataset

The Iris dataset contains:

- 150 samples
- 4 features
- 3 classes

The dataset is split into:

- Training set: 110 samples
- Test set: 40 samples

## Implementation

The nearest neighbor is found using:

```python
dist = np.sqrt(np.sum((X_train - x) ** 2, axis=1))
min_index = np.argmin(dist)
return y_train[min_index]
