from flask import Flask, render_template, request, send_file
from model import predict_sentiment
import csv

app = Flask(__name__)

history = []

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    confidence = 0
    emoji = ""
    color = ""

    if request.method == "POST":
        user_input = request.form["text"]

        result, confidence = predict_sentiment(user_input)

        if result == "positive":
            emoji = "😊"
            color = "green"
        else:
            emoji = "😞"
            color = "red"

        history.append({
            "text": user_input,
            "result": result,
            "confidence": confidence
        })

    return render_template("index.html", result=result, confidence=confidence,
                           emoji=emoji, color=color, history=history)


@app.route("/download")
def download():
    with open("history.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Text", "Sentiment", "Confidence"])

        for item in history:
            writer.writerow([item["text"], item["result"], item["confidence"]])

    return send_file("history.csv", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)