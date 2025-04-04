from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load Sentiment Analysis Model
sentiment_pipeline = pipeline("sentiment-analysis")

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get("text", "")
    
    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = sentiment_pipeline(text)[0]
    return jsonify({
        "sentiment": result['label'],
        "confidence": result['score']
    })

if __name__ == '__main__':
    app.run(debug=True)
