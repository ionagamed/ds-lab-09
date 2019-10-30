from flask import Flask, request, render_template
from pymongo import MongoClient


client_url = ",".join(
    f"mongodb-replicaset-{i}.mongodb-replicaset"
    for i in range(3)
)

client = MongoClient(client_url, 27017)
db = client.chat.messages
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        doc = {
            "username": request.form["username"],
            "message": request.form["message"],
        }
        db.insert_one(doc)

    messages = reversed(list(db.find()))

    return render_template("index.html", messages=messages)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

