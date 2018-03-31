from flask import Flask, request, current_app
from functools import wraps
from genexp import gen_exp

app = Flask(__name__)
#api = Api(app)

LETTERS = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e"}

def to_json(func):
    d = {}
    question, answer, opts = func()

    opts = sorted(opts)
    for i in opts:
        if "ERROR" in i.upper():
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
    return jsonp(to_json(gen_exp))

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == "__main__":
    app.run()
    