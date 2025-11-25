# movie-recommender-system
# Movie Recommendation System (Content-Based Filtering)

##  Project Overview
This project implements a **Content-Based Movie Recommendation System** that recommends similar movies based on their metadata such as genres, keywords, cast, crew, and overview.  
It uses **NLP vectorization (CountVectorizer)** and **Cosine Similarity** to calculate similarity scores between movies.

The project includes:
- Python script (`movie_recommender.py`)
- Jupyter Notebook (`movie_recommender.ipynb`)
- Dataset (`movie_dataset.csv`)
- Streamlit Web App (`app.py`)
- Documentation (README)

##  Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- NLP (CountVectorizer)  
- Cosine Similarity  
- Streamlit  
- Jupyter Notebook  

##  Project Structure
movie-recommendation-system/
├── movie_dataset.csv
├── movie_recommender.py
├── movie_recommender.ipynb
├── app.py
└── README.md

##  How the Model Works
1️⃣ Dataset Loading
The system loads and processes metadata from movie_dataset.csv.

2️⃣ Feature Engineering
Selected features:
Genres
Keywords
Cast
Crew
Overview
They are merged into a single text string.

3️⃣ Text Vectorization
Using CountVectorizer, text is converted into numerical vectors.

4️⃣ Similarity Calculation
Cosine similarity creates a similarity matrix:
[ Movie A   vs Movie B ]
[ Movie A   vs Movie C ]
...

5️⃣ Recommendation Logic
The recommend(movie) function:
Finds the index of the movie
Retrieves similarity scores
Sorts them
Returns Top 5 similar movies

## How to Run the Project
### Option A — Python Script
open python shell
python movie_recommender.py


### Option B — Jupyter Notebook
open jupyter notebook
load movie_recommender.ipynb
run-> run all cells

### Option C — Streamlit App
streamlit run app.py

### Sample Output

Top 5 recommendations for 'Inception':

1. Interstellar
2. Shutter Island
3. The Prestige
4. Memento
5. Tenet

### Future Enhancements

You can extend the project by adding:
✔ Movie posters (TMDB API)\
✔ Movie descriptions in output\
✔ Ratings and popularity\
✔ Hybrid recommendation system\
✔ Deployment on Streamlit Cloud

### Why This Project Is Valuable

This project demonstrates:

Data preprocessing
NLP & text vectorization
Machine Learning fundamentals
Recommender system logic
Clean Python code
Interactive UI with Streamlit
Industry-relevant skills for Data Analyst / ML roles

## 👤 Author
**Pandikkani Pandiyarajan**  
GitHub: github.com/PandikkaniPandiyarajan
