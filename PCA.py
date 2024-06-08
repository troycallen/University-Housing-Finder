from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Standardize the feature matrix
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)  # Reduce the dimensionality to 2
X_pca = pca.fit_transform(X_scaled)

loadings = pd.DataFrame(pca.components_, columns=X.columns, index=[f'PC{i+1}' for i in range(pca.n_components_)])
print("Principal Components (Loadings):")
print(loadings)

# Display the transformed features
# print("PCA transformed features:")
# print(X_pca)

# Display the explained variance ratio
print("\nExplained variance ratio:")
print(pca.explained_variance_ratio_

