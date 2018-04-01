from flask import Flask, request, current_app, jsonify
from functools import wraps
from genexp import gen_exp
from genslice import gen_slice
import random

app = Flask(__name__)

LETTERS = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e"}

def to_json(func):
    d = {}
    question, answer, opts = func()

    random.shuffle(opts)
    for i in opts:
        if "ERROR" in i.upper() or "ABOVE" in i.upper():
            opts.remove(i)
            opts.append(i)
            break

    for index, opt in enumerate(opts):
        d[LETTERS[index]] = opt
    d["question"] = question
    d["ans"] = LETTERS[opts.index(answer)]
    return d

def jsonp(func):
    """Wraps JSONified output for JSONP requests."""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            data = str(func(*args, **kwargs).data)
            content = str(callback) + '(' + data + ')'
            mimetype = 'application/javascript'
            return current_app.response_class(content, mimetype=mimetype)
        else:
            return func(*args, **kwargs)
    return decorated_function

@app.route('/exp')
def execute_gen_exp():
    return jsonify(to_json(gen_exp))

@app.route('/slice')
def execute_gen_slice():
    return jsonify(to_json(gen_slice))

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == "__main__":
    app.run()
    