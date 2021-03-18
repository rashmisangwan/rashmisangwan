from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn
import pandas as pd
from joblib import load
#from sklearn.tree import DecisionTreeClassifier
import jsonify

app = Flask(__name__)
print(pickle.__doc__)
#Load model

model = load('my.joblib')



@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about_handler():
  return '<h1> about </h1>'

@app.route('/contact')
def contact_handler():
  return '<h1> contact </h1>'

@app.route('/api/projects/basic_project', methods = ['GET'])
def project_handler():
  print(request.args)

  return { 'name': request.args.get('name'
  ) }




if __name__ == "__main__":
    app.run(debug=True)
