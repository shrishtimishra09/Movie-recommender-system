from flask import Flask, request, render_template, jsonify
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
from fuzzywuzzy import fuzz
import os

app = Flask(__name__)

# Use the correct file path to the dataset in the Docker container
dataset_path = '/app/moviesss.csv'  # The dataset will be copied into the /app directory in Docker
if os.path.exists(dataset_path):
    movies = pd.read_csv(dataset_path)
else:
    raise FileNotFoundError(f"Dataset not found at {dataset_path}")

def get_title_from_index(index):
    return movies.iloc[index]['movie_name']

def find_closest_title(title):
    leven_scores = list(enumerate(movies['movie_name'].apply(lambda x: fuzz.ratio(x, title))))
    sorted_leven_scores = sorted(leven_scores, key=lambda x: x[1], reverse=True)
    closest_title = get_title_from_index(sorted_leven_scores[0][0])
    return closest_title, sorted_leven_scores[0][1]

def get_index_from_title(title):
    return movies[movies.movie_name == title].index.values[0]

tfidf_vector = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vector.fit_transform(movies['genre'])
sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)

def get_recommendations(movie_user_likes, how_many=5):
    closest_title, score = find_closest_title(movie_user_likes)
    movie_index = get_index_from_title(closest_title)
    movie_list = list(enumerate(sim_matrix[int(movie_index)]))
    similar_movies = sorted(movie_list, key=lambda x: x[1], reverse=True)[1:how_many+1]
    return [get_title_from_index(i) for i, _ in similar_movies]

@app.route('/')
def home():
    return render_template('movie_recommendation_engine.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    movie_name = data.get("movie")
    recommendations = get_recommendations(movie_name)
    return jsonify(recommendations)

if __name__ == '__main__':
    # Run the app with host='0.0.0.0' so it can be accessed externally (important for Docker)
    app.run(debug=True, host='0.0.0.0', port=5000)
