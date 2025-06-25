from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
CORS(app)

# Load the dataset and model components once at startup
movies_data = pd.read_csv('movies.csv')
features = ['title', 'genres', 'keywords', 'tagline', 'director', 'cast']
for feature in features:
    movies_data[feature] = movies_data[feature].fillna('')
combined_features = movies_data['title'] + ' ' + movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['tagline'] + ' ' + movies_data['director'] + ' ' + movies_data['cast']
vectorizer = TfidfVectorizer()
feature_vector = vectorizer.fit_transform(combined_features)
similarity = cosine_similarity(feature_vector)

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    movie_name = data.get('movie', '')
    list_of_all_titles = movies_data['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    if not find_close_match:
        return jsonify({'error': 'Movie not found.'}), 404
    close_match = find_close_match[0]
    movie_index = movies_data[movies_data.title == close_match].index[0]
    similarity_score = list(enumerate(similarity[movie_index]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    recommendations = []
    i = 0
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = movies_data[movies_data.index == index]['title'].values[0]
        if title_from_index.lower() == close_match.lower():
            continue  # skip the input movie itself
        recommendations.append(title_from_index)
        i += 1
        if i >= 10:
            break
    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)
