import spacy
from flask import Flask, request, jsonify

# Load the spaCy language model
nlp = spacy.load('en_core_web_sm')

# Define your Flask application
app = Flask(__name__)

# Define your chatbot route
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = process_message(user_input)
    return jsonify({'response': response})

# Function to process user messages
def process_message(message):
    # Process the message using spaCy
    doc = nlp(message)
    
    # Example: Check for greetings
    if any(token.text.lower() in ['hello', 'hi', 'hey'] for token in doc):
        return "Hello! How can I assist you today?"
    
    # Example: Check for Fitistan events
    elif any(token.text.lower() in ['fitistan', 'kargil', 'upcoming', 'challenge', 'event'] for token in doc):
        return "Please navigate to https://www.fitistan.com/ to see our ongoing and upcoming events."
    
    # Example: Check for Android app install
    elif any(token.text.lower() in ['android', 'androids', 'google play'] for token in doc):
        return "For Android - download our apps from https://play.google.com/store/apps/details?id=io.ionic.fitistan"
    
    # Example: Check for iPhone app install
    elif any(token.text.lower() in ['ios', 'iphone', 'apple store'] for token in doc):
        return "For iPhone - please go to app.fitistan.com"
    
    # Default response
    else:
        return "I'm sorry, I didn't understand that."

# Run the Flask application
if __name__ == '__main__':
    app.run(port=5000)
