# Content Based Filtering 
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
apartment_data = pd.read_csv('/content/Housing Form Edited for Content Based Filtering.csv')
user_profile = {
    'location': 'Atlantic Station',
    'rent': 900,
    'number_of_roommates': 3,
    'House_Layout': '2B2B',
    'House_Type': 'Apartment'
}
def create_apartment_profile(apartment):
    return ' '.join([
        apartment['location'],
        str(apartment['rent']),
        str(apartment['number_of_roommates']),
        apartment['House_Layout'],
        apartment['House_Type']
    ])
apartment_data['profile'] = apartment_data.apply(create_apartment_profile, axis=1)
vectorizer = CountVectorizer().fit_transform(apartment_data['profile'])
similarity_scores = cosine_similarity(vectorizer)
# Create a CountVectorizer object
vectorizer = CountVectorizer()

# Fit the vectorizer to the apartment descriptions
vectorizer.fit(apartment_data['profile'])

# Transform the apartment descriptions to a matrix of token counts
apartment_matrix = vectorizer.transform(apartment_data['profile'])

# Transform the user profile to a matrix of token counts
user_vector = vectorizer.transform([create_apartment_profile(user_profile)])

# Compute cosine similarities between the user profile and the apartment matrix
user_scores = cosine_similarity(user_vector, apartment_matrix)[0]

# Sort apartments by cosine similarity scores in descending order
recommended_apartments = apartment_data.iloc[user_scores.argsort()[::-1]]
print(recommended_apartments.head())
# Property Assessment
assessment_features = [ 'location',
    'rent',
    'number_of_roommates',
    'House_Layout',
    'House_Type']
# Select a sample apartment for assessment
apartment = apartment_data.sample()

# Create an apartment profile for assessment
apartment_profile = create_apartment_profile(apartment.iloc[0])

# Transform the apartment profile to a matrix of token counts
apartment_vector = vectorizer.transform([apartment_profile])

# Calculate the cosine similarities between the sample apartment and all other apartments
similarities = cosine_similarity(apartment_vector, apartment_matrix)

# Get the similarity scores for all apartments except for the sample apartment
similarity_scores = similarities[0, :].tolist()
similarity_scores.pop(apartment.index[0])

# Get the assessment feature values for the sample apartment and convert them to numerical types
assessment_values = apartment[assessment_features].apply(pd.to_numeric, errors='coerce').values.tolist()[0]

# Calculate the average feature values of the most similar apartments and convert them to numerical types
similar_apartment_features = apartment_data.loc[similarity_scores.index(max(similarity_scores)), assessment_features].apply(pd.to_numeric, errors='coerce').tolist()

# Calculate the percentage difference between the sample apartment and the average features of the most similar apartments
assessment_results = [(similar_apartment_features[i] - assessment_values[i])/assessment_values[i]*100 for i in range(len(assessment_features)) if not pd.isna(similar_apartment_features[i]) and not pd.isna(assessment_values[i])]

# Print the assessment results
for i in range(len(assessment_results)):
    print(f'{assessment_features[i]}: {assessment_values[i]}')
    print(f'Average {assessment_features[i]} of most similar apartments: {similar_apartment_features[i]}')
    print(f'Percentage difference: {assessment_results[i]:.2f}%')
