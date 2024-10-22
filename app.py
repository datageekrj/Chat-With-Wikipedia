from flask import Flask, render_template, request, jsonify
import json
import google.generativeai as genai
from helper import get_wikipedia_page_text

app = Flask(__name__)
with open("api_key.json", "r") as file:
    data = json.load(file)

genai.configure(api_key=data["key"])

model = genai.GenerativeModel('gemini-pro')

def send_message(message, history):
    history.append({"role":"model", "parts":"Okay, I will take care of this in mind and will not forget it."})
    chat = model.start_chat(history = history)
    response = chat.send_message(message)
    return response.text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    history = request.json.get('history')
    history_new = [{"role":"user", "parts" : "Please use the below information to answer any questions: " + history[0].get("parts")}]
    response = send_message(user_message, history_new)
    return jsonify({'message': response})

@app.route("/get_wiki_text", methods = ["POST"])
def get_wiki_text():
    title = request.json.get('title')
    wiki_response = get_wikipedia_page_text(title)
    if wiki_response == 0:
        jsonify({"error" : "The wiki page with that title does not exist"})
    print(wiki_response)
    return jsonify({'text': wiki_response})

if __name__ == '__main__':
    app.run(debug=True)
