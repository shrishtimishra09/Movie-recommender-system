# Movie-recommender-system
A web-based Movie Recommendation System built using Flask, Python, and a machine learning algorithm. This system suggests movies to users based on the movie they input, utilizing content-based filtering and fuzzy matching techniques.

Features
User Input: Users can input a movie name to get a list of movie recommendations.

Recommendation Algorithm: The system uses content-based filtering with TF-IDF and cosine similarity, enhanced by fuzzy string matching for movie name accuracy.

Real-time Recommendations: Once the user enters a movie name, the system provides a list of recommended movies in real-time.

Technologies Used
Python: Programming language used to build the backend.

Flask: Python web framework used to serve the application.

Pandas: Used to handle and process the movie dataset (CSV file).

Scikit-learn: Used for implementing the recommendation algorithm (TF-IDF and cosine similarity).

FuzzyWuzzy: Used for fuzzy matching movie names to handle spelling variations.

HTML/CSS: Frontend technologies for creating a simple yet elegant user interface.

JavaScript: For making asynchronous calls to the backend for real-time recommendations.

Project Setup
Prerequisites
Before running the project, ensure you have the following installed:

Python 3.x

pip (Python package manager)

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/shrishtimishra09/movie-recommender-system.git
cd movie-recommender-system
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Ensure the movie dataset (moviesss.csv) is in the project directory.

Run the application:

bash
Copy
Edit
python app.py
The app will be running at http://127.0.0.1:5000/.

Usage
Open your browser and go to http://127.0.0.1:5000/.

Enter a movie name in the search bar.

Click on "Get Recommendations" to receive a list of recommended movies.

Deployment
This project can be deployed on cloud platforms like Heroku, Render, or Vercel using Docker for containerization.

Project Structure
perl
Copy
Edit
movie-recommender-system/
├── app.py                # Flask app to handle backend logic
├── moviesss.csv          # Movie dataset (CSV format)
├── requirements.txt      # Python dependencies
├── templates/            # HTML templates
│   └── movie_recommendation_engine.html
└── Dockerfile            # Dockerfile for containerizing the app
License
This project is licensed under the MIT License - see the LICENSE file for details.
