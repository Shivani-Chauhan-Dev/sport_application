from flask import Flask, render_template, request, jsonify, json
import requests

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_massage = request.data
    print(user_massage)
    rasa_response = requests.post(RASA_URL, user_massage)
    print(rasa_response.json())
    return rasa_response.json()









if __name__=="__main__":
    app.run(debug=True,port=8080)