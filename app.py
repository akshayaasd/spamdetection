from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def detect_spam(message):
    # Define a list of spam keywords or patterns
    spam_keywords = ['buy now', 'click here', 'limited offer', 'money back guarantee']
    
    # Check if any spam keyword is present in the message
    for keyword in spam_keywords:
        if re.search(keyword, message, re.IGNORECASE):
            return True
    
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect_spam', methods=['POST'])
def detect_spam_route():
    message = request.form['message']
    
    if detect_spam(message):
        response = {'spam': True, 'message': 'Spam message detected!'}
    else:
        response = {'spam': False, 'message': 'Message is not spam.'}
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
