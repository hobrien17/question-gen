from flask import Flask, request, jsonify
from genexp import gen_exp

app = Flask(__name__)

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

@app.route('/exp')
def execute_gen_exp():
    return jsonify(to_json(gen_exp))

if __name__ == "__main__":
    app.run()
    