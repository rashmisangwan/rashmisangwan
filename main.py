from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import sklearn
#import pandas as pd
from joblib import load
#from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)
# Load model

pkl_filename = "drug_tree.pkl"
with open(pkl_filename, 'rb') as f:
    model = pickle.load(f)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/api/projects/basic_project', methods=['GET'])
def project_api_handler():
    a = request.args.to_dict()
    print(a)
    b = list(a.values())
    c = []
    for i in range(len(b)):
        if i == 0:
            c.append(int(b[i]))
        elif i == 4:
            c.append(float(b[i]))
        else:
            c.append(b[i])
    X = np.array([c], dtype='object')

    from sklearn import preprocessing
    le_sex = preprocessing.LabelEncoder()
    le_sex.fit(['F', 'M'])
    X[:, 1] = le_sex.transform(X[:, 1])

    le_BP = preprocessing.LabelEncoder()
    le_BP.fit(['LOW', 'NORMAL', 'HIGH'])
    X[:, 2] = le_BP.transform(X[:, 2])

    le_Chol = preprocessing.LabelEncoder()
    le_Chol.fit(['NORMAL', 'HIGH'])
    X[:, 3] = le_Chol.transform(X[:, 3])

    print(X, "rashmi")
    print("your drug is : ", model.predict(X))

    return jsonify({'input': {'age': a['age'], 'sex': a['sex'], "BP": a['BP'], "colestrol": a['Cholesterol'], "na_to_k": a['Na_to_K']},
                    'output': {"drug_suggested": str(model.predict(X)[0])}
                    })
    # return { 'name': request.args.get('name') }



@app.route('/projects/basic_project', methods=['GET', "POST"])
def project_handler():
    if request.method == 'POST':
        a = request.form.to_dict()
        print(a)
        b = list(a.values())
        c = []
        for i in range(len(b)):
            if i == 0:
                c.append(int(b[i]))
            elif i == 4:
                c.append(float(b[i]))
            else:
                c.append(b[i])
        X = np.array([c], dtype='object')

        from sklearn import preprocessing
        le_sex = preprocessing.LabelEncoder()
        le_sex.fit(['F', 'M'])
        X[:, 1] = le_sex.transform(X[:, 1])

        le_BP = preprocessing.LabelEncoder()
        le_BP.fit(['LOW', 'NORMAL', 'HIGH'])
        X[:, 2] = le_BP.transform(X[:, 2])

        le_Chol = preprocessing.LabelEncoder()
        le_Chol.fit(['NORMAL', 'HIGH'])
        X[:, 3] = le_Chol.transform(X[:, 3])
        
        print(X, "rashmi")
        print("your drug is : ", model.predict(X))

        output = str(model.predict(X)[0])

        return render_template('project_basic.html', data = {'input' : a, 'output': output})

    else:
        return render_template('project_basic.html')


if __name__ == "__main__":
    app.run(debug=True)
