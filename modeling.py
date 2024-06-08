import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample dataset
data = {
    'area': [1500, 2000, 2500, 3000, 3500],
    'bedrooms': [3, 4, 3, 5, 4],
    'age': [10, 20, 15, 5, 2],
    'rating': [4.0, 4.5, 4.2, 5.0, 4.8]
}

file_path = 'HousingForm.csv'
df = pd.read_csv(file_path)


# Features (X) and target (y) extraction
X = df[['Roommates', 'Rent', 'Footage', 'Distance']]
y = df['Overall']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
#print(y_pred)

print(f"Model Weights: {model.coef_}")
print(f"Model Bias: {model.intercept_}")
# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")

# # Predict ratings for new users
# new_data = np.array([
#     [1800, 3, 8],
#     [2200, 4, 12]
# ])

df2 = pd.read_csv('UpdatedOutput.csv')
X_new = df2[['Roommates', 'Rent', 'Footage', 'Distance']]
new_ratings = model.predict(X_new)
# print(f"Predicted Ratings: {new_ratings}")
# df2['Ratings'] = new_ratings
# df2.to_csv('LR_Ratings.csv')
