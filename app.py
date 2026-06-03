from flask import Flask, jsonify
from flask_cors import CORS

# Create the country/location service app
app = Flask(__name__)
CORS(app)

# Hardcoded list returned to the frontend
COUNTRIES = [
    {"name": "New York", "value": "new york"},
    {"name": "Sydney", "value": "sydney"},
    {"name": "Cape Town", "value": "cape town"},
    {"name": "Bangkok", "value": "bangkok"},
    {"name": "London", "value": "london"},
    {"name": "Tokyo", "value": "tokyo"},
]


@app.route("/countries", methods=["GET"])
def countries():
    return jsonify(COUNTRIES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

