# SVM Hyperparameter Selection using K-Fold Cross-Validation

A simple exercise demonstrating how to use **K-Fold Cross-Validation** to select the best `gamma` hyperparameter for an **SVM (Support Vector Machine)** with an RBF kernel.

## 📌 Objective

The goal is to understand how we can:

1. Split data into training and test sets.
2. Use K-Fold Cross-Validation on the training data.
3. Compare different `gamma` values.
4. Select the best `gamma` based on the average CV score.
5. Train the final SVM using the best configuration.
6. Evaluate the final model on the untouched test set.

---

## 🧠 Concept

The Iris dataset is first divided into:

```text
Full Dataset
     ↓
Train / Test Split
     ↓
Training Data        Test Data 🔒
     ↓
K-Fold CV
     ↓
Compare gamma values
     ↓
Choose best gamma
     ↓
Train final model
     ↓
Evaluate on Test Data
