import pickle
import numpy as np
from sklearn import preprocessing
import os

current_dir = os.path.dirname(__file__)
pkl_filename = current_dir + '/model.pkl'

with open(pkl_filename, 'rb') as f:
    model = pickle.load(f)

"""
    @params
    -------
    age: <int>
    gender: F | M
    bp: LOW | NORMAL | HIGH
    cholestrol: NORMAL | HIGH
    na_to_k: <float>

    @output
    -------
    drugA | drugB | drugC | drugX | drugY
"""


def run(data):
    age = data['age']
    gender = data['gender']
    bp = data['bp']
    cholestrol = data['cholestrol']
    na_to_k = data['na_to_k']

    X = np.array([[age, gender, bp, cholestrol, na_to_k]], dtype='object')

    le_gender = preprocessing.LabelEncoder()
    le_gender.fit(['F', 'M'])
    X[:, 1] = le_gender.transform(X[:, 1])

    le_BP = preprocessing.LabelEncoder()
    le_BP.fit(['LOW', 'NORMAL', 'HIGH'])
    X[:, 2] = le_BP.transform(X[:, 2])

    le_Chol = preprocessing.LabelEncoder()
    le_Chol.fit(['NORMAL', 'HIGH'])
    X[:, 3] = le_Chol.transform(X[:, 3])

    return model.predict(X)[0]
