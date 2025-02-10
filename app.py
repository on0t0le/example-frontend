from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

# Get API URL from environment variable, with fallback default
API_URL = os.getenv('API_URL', 'https://jsonplaceholder.typicode.com')

@app.route('/')
def index():
    # Fetch user data from API
    response = requests.get(f"{API_URL}/users")
    users = response.json()

    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=8080)
