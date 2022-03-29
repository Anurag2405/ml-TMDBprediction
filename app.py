from flask import Flask, redirect, render_template, request
import pandas as pd
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import xgboost

app = Flask(__name__)
model = pickle.load(open('proj.pkl', 'rb'))

@app.route("/", methods = ['GET','POST'])
def hello_world():
    if request.method == 'POST':
        budget = float(request.form['budget'])
        populatiry = float(request.form['populatiry'])
        runtime = float(request.form['runtime'])
        release_month = int(request.form['release_month'])
        release_day = int(request.form['release_day'])
        release_year = int(request.form['release_year'])
        release_dayofweek = int(request.form['release_dayofweek'])
        release_quarter = int(request.form['release_quarter'])
        is_released = int(request.form['is_released'])
        has_homepage = int(request.form['has_homepage'])
        has_a_tagline = int(request.form['has_a_tagline'])
        originallang_en = int(request.form['originallang_en'])
        has_collection = int(request.form['has_collection'])
        num_genres = int(request.form['num_genres'])
        # data = pd.DataFrame({"budget":budget,"populatiry":populatiry})
        # print(data["budget"])
        prediction=model.predict([[]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry prediction not available")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')
    # return render_template('index.html')


if __name__ == "__main__":
    app.run(debug = True)
