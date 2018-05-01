from flask import Flask, request, current_app, jsonify
from functools import wraps
from genexp import gen_exp
from genslice import gen_slice
from genlst import gen_list
from genstr import gen_str
from gendict import gen_dict
from genclass import gen_class
from genio import gen_io
from genexcept import gen_except
from geninh import gen_inh
import random

app = Flask(__name__)

LETTERS = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e"}

def to_json(inp):
    d = {}
    question, answer, opts = inp

    random.shuffle(opts)
    for i in opts:
        if i.upper().endswith("ERROR") or "ABOVE" in i.upper():
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
    return jsonify(to_json(gen_exp()))

@app.route('/slice')
def execute_gen_slice():
    return jsonify(to_json(gen_slice()))

@app.route('/list')
def execute_gen_list():
    return jsonify(to_json(gen_list()))

@app.route('/str')
def execute_gen_str():
    return jsonify(to_json(gen_str()))

@app.route('/dict')
def execute_gen_dict():
    return jsonify(to_json(gen_dict()))

@app.route('/class')
def execute_gen_class():
    return jsonify(to_json(gen_class()))

@app.route('/io')
def execute_gen_io():
    return jsonify(to_json(gen_io()))

@app.route('/except')
def execute_gen_except():
    return jsonify(to_json(gen_except()))

@app.route('/inh')
def execute_gen_inh():
    return jsonify(to_json(gen_inh()))

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == "__main__":
    app.run()
    