# Movie Recommendation System

This project is a content-based movie recommendation system with a web frontend and a Flask backend API.

## Features
- Enter a movie name and get top 10 similar movie recommendations.
- Modern, responsive HTML/CSS frontend.
- Python backend using Flask, pandas, scikit-learn, and difflib.
- CORS enabled for easy frontend-backend communication.

## Getting Started

### 1. Install Requirements
Install Python packages:
```bash
pip install flask flask-cors pandas scikit-learn
```

### 2. Prepare Data
Ensure `movies.csv` is present in the project directory. This file should contain columns: `title`, `genres`, `keywords`, `tagline`, `director`, `cast`.

### 3. Run the Backend
Start the Flask API server:
```bash
python movie_recommendation_api.py
```
The server will run at `http://localhost:5000/`.

### 4. Use the Frontend
Open `movie_recommendation_frontend.html` directly in your web browser. Enter a movie name and click "Get Recommendations".

## API Usage
- **Endpoint:** `POST /api/recommend`
- **Request JSON:** `{ "movie": "Movie Name" }`
- **Response JSON:** `{ "recommendations": ["Movie1", "Movie2", ...] }`

## Notes
- The backend is not case sensitive for movie names.
- If you want to access the backend from another device, run the Flask app with `app.run(host='0.0.0.0', debug=True)` and use your computer's IP address in the frontend.
- For production, use a WSGI server (not Flask's built-in server).

## Project Structure
```
Movie-Recommendation-System/
├── movie_recommendation_api.py         # Flask backend
├── movie_recommendation_frontend.html  # HTML/CSS/JS frontend
├── movies.csv                          # Movie dataset
├── README.md                           # Documentation
```
