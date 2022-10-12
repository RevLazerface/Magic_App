from flask import Flask, render_template
import csv
import os
import random

app = Flask(__name__)

script_dir = os.path.dirname(__file__)
s = 'static/wild_magic.csv'
path = os.path.join(script_dir, s)

with open(path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    keys = csv_reader.fieldnames
    effects = list(csv_reader)

@app.route("/")
def home():
    return render_template("main.html")


@app.route("/effect", methods=['POST'])
def effect():
    d20 = random.randint(1,20)
    d100 = random.randint(1,100)

    if 1 <= d20 <=3:
        effect = effects[d100][keys[1]]
    elif 4 <= d20 <= 9:
        effect = effects[d100][keys[2]]
    elif 10 <= d20 <=20:
        effect = effects[d100][keys[3]]

    return render_template("effect.html", effect=effect)


if __name__ == "__main__":
    app.run(debug=True)