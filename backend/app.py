
from flask import Flask, request, jsonify
from model import load_assets, find_path


app = Flask(__name__)


load_assets()

@app.route("/")
def home():
    return "Backend running"


@app.route("/find-path", methods=["POST"])
def get_path():
   
    data = request.get_json()
    source = data.get("source_idx")
    target = data.get("target_idx")

    
    result = find_path(source, target)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)