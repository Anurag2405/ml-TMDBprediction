# TMDB BOX Office prediction:
# Flight Fare Prediction: 

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [Future scope of project](#future-scope)


## Demo
Link: [http://anurag-tmdbprediction.herokuapp.com/](http://anurag-tmdbprediction.herokuapp.com/)

![](https://i.imgur.com/3OyNtUI.png)

![](https://i.imgur.com/5tEsR4j.png)

## Overview
This is a Flask web app which predicts Box office revenue of movies.

## Installation
The Code is written in Python 3. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Deployement on Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project.

[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

Our next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Directory Tree 
```
├── templates
│   ├── index.html
├── Procfile
├── README.md
├── app.py
├── movie-boxoffice.ipynb
├── data.pickle
├── requirements.txt
```

## Technologies Used
<h3> Tools used for project development: </h3>
<ul>
<li><p><b>Python ( 3.7 version)</b></p></li>
<li><p><b>Flask</b></p></li>
<li><p><b>Scikit learn</b></p></li>
<li><p><b>Pandas</b></p></li>
<li><p><b>Numpy</b></p></li>
<li><p><b>HTML</b></p></li>
<li><p><b>Bootstrap</b></p></li>
</ul>

## Future Scope

* Use multiple Algorithms
* Optimize Flask app.py
* Front-End
* Creating an API to directly use the model
