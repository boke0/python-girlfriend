import openai
import os
from flask import Flask, jsonify, request
from flask_cors import CORS

# Set the API key
openai.api_key = os.environ.get('CHAT_GPT_API_KEY')

app = Flask(__name__)
CORS(app)


@app.post('/v1/prompt')
def post_prompt():
    req = request.get_json()
    print("prompt:", req["prompt"])
    response = openai.Completion.create(
        engine="davinci",
        prompt=req["prompt"],
    )
    print(response)
    return jsonify({
        "message": response["choices"][0]["text"]
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=os.environ.get("PORT"),
        debug=os.environ.get("ENV") == "development"
    )
