import streamlit as st
import joblib

def iris_flower_classification(sepal_length, sepal_width, petal_length, petal_width, selected_model):
    prediction = selected_model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    if prediction == 0:
        return 'Iris Setosa', 'https://upload.wikimedia.org/wikipedia/commons/1/11/Iris_setosa_2.jpg'
    elif prediction == 1:
        return 'Iris Versicolor', 'https://upload.wikimedia.org/wikipedia/commons/2/27/Blue_Flag%2C_Ottawa.jpg'
    else:
        return 'Iris Virginica', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/1200px-Iris_virginica_2.jpg'

st.title('Iris Flower Classification')

sepal_length = st.sidebar.slider('Sepal Length', 4.3, 7.9, 5.0)
sepal_width = st.sidebar.slider('Sepal Width', 2.0, 4.4, 3.0)
petal_length = st.sidebar.slider('Petal Length', 1.0, 6.9, 3.0)
petal_width = st.sidebar.slider('Petal Width', 0.1, 2.5, 0.3)

models = joblib.load('all_models.pkl')

selected_model = st.selectbox('Select Model', models)

flower_name, flower_image = iris_flower_classification(sepal_length, sepal_width, petal_length, petal_width, selected_model)
st.markdown('Flower Name: <span style="color:red">{}</span>'.format(flower_name), unsafe_allow_html=True)
st.image(flower_image, width=300)