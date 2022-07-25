import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")

st.image("data:image/jpeg;base64,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")
st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

iris = pd.read_csv('https://raw.githubusercontent.com/SSofiah/Iris_July/main/IRIS.csv')
X = iris.drop('species',axis = 1)
Y = iris['species']

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(['Iris-setosa','Iris-versicolor','Iris-virginica'])

st.subheader('Prediction')
#st.write(iris.target_names[prediction])
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
