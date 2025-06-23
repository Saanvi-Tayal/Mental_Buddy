from flask import Flask, request, jsonify, render_template
from chatbot import get_chatbot_response

app = Flask(__name__)

# API endpoint for chatbot responses
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message', '')
    if not user_input:
        return jsonify({'response': 'Please provide a message.'}), 400
    response = get_chatbot_response(user_input)
    return jsonify({'response': response})

# Serve the frontend
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)