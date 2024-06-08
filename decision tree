from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
# Create and fit the model
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")

df2 = pd.read_csv('UpdatedOutput.csv')
X_new = df2[['Roommates', 'Rent', 'Footage', 'Distance']]
new_ratings = model.predict(X_new)
print(f"Predicted Ratings: {new_ratings}")
# df2['Ratings'] = new_ratings
# df2.to_csv('DT_Ratings.csv')
