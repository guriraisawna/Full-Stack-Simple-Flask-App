from flask import Flask, jsonify

app = Flask(__name__, static_url_path='', static_folder='')

@app.get("/")
def index():
    return "Welcome to REST API!"

@app.get("/api/v1/cat")
def get_cat():
    cat = [{
        "cat_id": "7218",
        "name": "Pyarry",
        "birthdate": "2009-12-05",
        "image": "https://pixabay.com/images/search/small%20cat/",
        "weight": 8,
        "owner": "Gurpreet Singh"
    }]
    return jsonify(cat)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)