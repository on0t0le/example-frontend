from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/add_user', methods=['POST'])
def create_user():
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    
    # Create new user through API
    response = requests.post(f"{API_URL}/users", json={
        'name': name,
        'email': email
    })
    
    return redirect(url_for('index'))

@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    # Send delete request to API
    response = requests.delete(f"{API_URL}/users/{user_id}")
    
    # Redirect back to index page after deletion
    return redirect(url_for('index'))

    # Redirect back to index page
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=8080)
