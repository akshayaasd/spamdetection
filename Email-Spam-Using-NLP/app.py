from flask import Flask, request, jsonify, render_template
import pickle

# Load the trained model and vectorizer
with open('models/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
with open('models/vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Initialize the Flask app
app = Flask(__name__)

# Define a route for predicting spam
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the data from the request
        data = request.json
        message = data['message']
        
        # Ensure vectorizer is a CountVectorizer object and use transform method correctly
        message_vec = vectorizer.transform([message])  # Transform the message using the loaded vectorizer
        prediction = model.predict(message_vec)  # Predict using the trained model
        
        # Map prediction to output label
        output = 'spam' if prediction[0] == 1 else 'not spam'
        
        return jsonify({'prediction': output})
    except Exception as e:
        return jsonify({'error': str(e)})

# Define a home route
@app.route('/')
def home():
    return render_template('index.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
