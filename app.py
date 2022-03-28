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
        release_day = request.form['release_day']
        release_year = request.form['release_year']
        release_dayofweek = request.form['release_dayofweek']
        is_released = request.form['is_released']
        has_homepage = request.form['has_homepage']
        has_a_tagline = request.form['has_a_tagline']
        originallang_en = request.form['originallang_en']
        has_collection = request.form['has_collection']
        num_genres = request.form['num_genres']
        print(has_a_tagline)
        print(type(has_a_tagline))
        # data = pd.DataFrame({"budget":budget,"populatiry":populatiry})
        # print(data["budget"])
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug = True)
