from flask import Flask, request, jsonify
from genexp import gen_exp

app = Flask(__name__)

@app.route('/exp')
def execute_gen_exp():
    return jsonify({"a": 1})

if __name__ == "__main__":
    app.run()
    