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
