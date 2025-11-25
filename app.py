import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_excel("movie_dataset.xlsx")

# Preprocessing
for col in ['overview', 'genres', 'keywords', 'cast', 'crew']:
    movies[col] = movies[col].fillna('')

movies['tags'] = (
    movies['overview'] + " " +
    movies['genres'] + " " +
    movies['keywords'] + " " +
    movies['cast'] + " " +
    movies['crew']
)

# Vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

# Similarity Matrix
similarity = cosine_similarity(vectors)

# Recommendation Function
def recommend(movie):
    movie = movie.strip()

    if movie not in movies['title'].values:
        return ["Movie not found in database."]

    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    return [movies.iloc[i[0]].title for i in movie_list]


# Streamlit UI
st.title("🎬 Movie Recommendation System")
st.write("Select a movie to get top 5 similar movie recommendations.")

movie_list = movies['title'].values
selected_movie = st.selectbox("Choose a movie", movie_list)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.write("### 🎯 Recommended Movies:")
    for r in recommendations:
        st.write("- " + r)
