from flask import Flask, redirect, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def hello_world():
    if request.method == 'POST':
        budget = request.form['budget']
        populatiry = request.form['populatiry']
        runtime = request.form['runtime']
        release_quarter = request.form['release_quarter']
        release_month = request.form['release_month']
        data = pd.DataFrame({"budget":budget,"populatiry":populatiry})
        print(data["budget"])
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug = True)
