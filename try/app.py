from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Flask Chatbot')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message").lower()
    
    if "hello" in user_message:
        bot_response = "Hello! How are you?"
    elif "how are you" in user_message:
        bot_response = "I'm just a bot, but I'm doing great! How about you?"
    elif "bye" in user_message:
        bot_response = "Goodbye! Have a great day!"
    else:
        bot_response = f"You said: {user_message}"
    
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
