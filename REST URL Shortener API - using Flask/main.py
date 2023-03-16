from flask import Flask, request, jsonify, render_template, redirect
import string
import random
import validators
from datetime import datetime, timedelta

app = Flask(__name__)

url_db = {}  # This will be our in-memory database for storing URLs


# Function to generate random string of fixed size
def generate_random_string(size=10):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))


# Route to serve HTML form for creating short URLs
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


# Route to create short URL for given input URL
@app.route('/create', methods=['POST'])
def create_short_url():
    input_url = request.form['url']
    if not validators.url(input_url) or len(input_url) > 250:
        return jsonify({'error': 'Invalid URL or URL length greater than 250 characters.'}), 400

    if 'custom_name' in request.form:
        custom_name = request.form['custom_name']
        if custom_name in url_db:
            return jsonify({'error': 'Custom name already exists.'}), 400
        short_name = custom_name
    else:
        short_name = generate_random_string()

    url_db[short_name] = {'url': input_url, 'created_at': datetime.utcnow()}
    short_url = request.host_url + short_name
    return render_template('short_url.html', short_url=short_url)


# Route to display original URL for given short URL
@app.route('/<short_name>', methods=['GET'])
def display_original_url(short_name):
    if short_name not in url_db:
        return jsonify({'error': 'Short URL does not exist.'}), 404

    url_db[short_name]['access_count'] = url_db[short_name].get('access_count', 0) + 1
    return redirect(url_db[short_name]['url'], code=302)


# Function to automatically delete URLs older than 30 days
def delete_old_urls():
    for short_name, url_data in url_db.items():
        if datetime.utcnow() - url_data['created_at'] > timedelta(days=30):
            del url_db[short_name]


if __name__ == '__main__':
    app.run(debug=True)
