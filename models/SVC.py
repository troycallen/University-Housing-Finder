from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix


df['Label'] = (df['Overall'] >= 8.0).astype(int)
y = df['Label']
# Standardize the feature matrix (both training and testing sets)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train the SVM classifier
svm_classifier = SVC(kernel='linear', C=1)
svm_classifier.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = svm_classifier.predict(X_test_scaled)

# Evaluate the classifier
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

from sklearn.pipeline import make_pipeline
# SVM with cross-validation
svm = make_pipeline(StandardScaler(), SVC(random_state=42))  # StandardScaler is used to normalize the features
svm_scores = cross_val_score(svm, X, y, cv=3)  # 5-fold cross-validation
svm_mean_score = svm_scores.mean()
print(f"SVM mean accuracy: {svm_mean_score:.2f}")

# Base model: Decision Tree
base_model = SVC(random_state=42)

# Bagging
bagging = BaggingClassifier(estimator=base_model, n_estimators=100, random_state=42)
bagging_scores = cross_val_score(bagging, X, y, cv=3)  # 3-fold cross-validation
bagging_mean_score = bagging_scores.mean()
print(f"Bagging mean accuracy: {bagging_mean_score:.2f}")

# Boosting (using Gradient Boosting)
boosting = GradientBoostingClassifier(n_estimators=100, random_state=42)
boosting_scores = cross_val_score(boosting, X, y, cv=3)  # 3-fold cross-validation
boosting_mean_score = boosting_scores.mean()
print(f"Boosting mean accuracy: {boosting_mean_score:.2f}")

