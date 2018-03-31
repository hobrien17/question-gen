from flask import Flask, request
from genexp import gen_exp

app = Flask(__name__)

@app.route('/exp')
def execute_gen_exp():
    return gen_exp()

if __name__ == "__main__":
    app.run()
    