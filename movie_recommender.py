
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_excel('movie_dataset.xlsx')

# Fill missing values
for col in ['overview', 'genres', 'keywords', 'cast', 'crew']:
    movies[col] = movies[col].fillna('')

# Combine relevant text columns
movies['tags'] = movies['overview'] + ' ' + movies['genres'] + ' ' + movies['keywords'] + ' ' + movies['cast'] + ' ' + movies['crew']

# Convert text to vectors
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

# Compute cosine similarity
similarity = cosine_similarity(vectors)

# Recommendation function
def recommend(movie):
    if movie not in movies['title'].values:
        print("Movie not found in database.")
        return
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    print(f"Recommendations for {movie}:")
    for i in movie_list:
        print(movies.iloc[i[0]].title)

# Example
recommend("Joker")
