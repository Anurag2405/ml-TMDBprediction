from flask import Flask, redirect, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
with open('data.pickle', 'rb') as f:
    data = pickle.load(f)
model = data
@app.route("/", methods = ['GET','POST'])
def hello_world():
    if request.method == 'POST':
        # getting the input from the form
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
    
        # creating a dataframe from which will be an input to the model
        new_input = {
            'budget': budget,
            'populatiry': populatiry,
            'runtime': runtime,
            'release_month': release_month,
            'release_day': release_day,
            'release_year': release_year,
            'release_dayofweek': release_dayofweek,
            'release_quarter':release_quarter,
            'is_released':is_released,
            'has_homepage':has_homepage,
            'has_a_tagline':has_a_tagline,
            'originallang_en':originallang_en,
            'has_collection':has_collection,
            'num_genres':num_genres,
        }
        new_input_df = pd.DataFrame([new_input])
        # predicting the value
        prediction = model.predict(new_input_df)
        # print(np.expm1(prediction[0]))
        output= np.expm1(prediction[0])
        if output<0:
            return render_template('index.html',prediction_texts="Sorry prediction not available")
        else:
            return render_template('index.html',prediction_text="The predicted revenue is {}".format(output))
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug = True)
