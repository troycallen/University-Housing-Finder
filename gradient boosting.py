from sklearn.ensemble import BaggingClassifier, GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
# Base model: Decision Tree
base_model = DecisionTreeClassifier(random_state=42)

# Bagging
bagging = BaggingClassifier(estimator=base_model, n_estimators=100, random_state=42)
bagging_scores = cross_val_score(bagging, X, y, cv=3)  # 5-fold cross-validation
bagging_mean_score = bagging_scores.mean()
print(f"Bagging mean accuracy: {bagging_mean_score:.2f}")

# Boosting (using Gradient Boosting)
boosting = GradientBoostingClassifier(n_estimators=100, random_state=42)
boosting_scores = cross_val_score(boosting, X, y, cv=3)  # 5-fold cross-validation
boosting_mean_score = boosting_scores.mean()
print(f"Boosting mean accuracy: {boosting_mean_score:.2f}"
