#!/bin/bash

# Define the app directory
APP_DIR="flask_app"

# Create the main application directory
mkdir -p $APP_DIR

# Navigate to the application directory
cd $APP_DIR

# Create directories for templates and static files
mkdir -p templates static

# Create a basic HTML file
cat > templates/index.html <<EOL
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Simple Web Scraper</title>
</head>
<body>
<h1>Simple Web Scraper Interface</h1>
<input type="text" id="urlToScrape" placeholder="Enter URL to scrape">
<button onclick="scrape()">Scrape</button>
<p id="result"></p>

<script src="/static/script.js"></script>
</body>
</html>
EOL

# Create a basic JavaScript file
cat > static/script.js <<EOL
function scrape() {
  var url = document.getElementById('urlToScrape').value;
  
  fetch('/scrape', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ url: url }),
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById('result').textContent = JSON.stringify(data);
  })
  .catch((error) => {
    console.error('Error:', error);
  });
}
EOL

# Create the Flask Python script
cat > scraper.py <<EOL
from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json
    url = data['url']
    result = {}
    try {
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title').get_text()
        result['title'] = title
    except Exception as e:
        result['error'] = str(e)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
EOL

echo "Flask app directory structure is ready."
