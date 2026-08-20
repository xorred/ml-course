from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.svm import SVC

configs = [0.1, 1, 0.4, 0.2]
scores = {}

iris = load_iris()

X = iris.data
y = iris.target

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# K-Fold Cross-Validation
for config in configs:

    model = SVC(kernel="rbf", gamma=config)

    scores[config] = cross_val_score(
        model,
        X_train,
        y_train,
        cv=6
    ).mean()

# Select best gamma
best = max(scores, key=scores.get)

print("Scores:", scores)
print("Best gamma:", best)
print("Best CV score:", scores[best])

# Train final model using best gamma
best_model = SVC(kernel="rbf", gamma=best)

best_model.fit(X_train, y_train)

# Evaluate on untouched test set
test_accuracy = best_model.score(X_test, y_test)

print("Test accuracy:", test_accuracy)
