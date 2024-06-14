import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
from io import BytesIO
import joblib

models={
    'logistic_regression':joblib.load('logr_model.pkl'),
    'Decision_tree':joblib.load('decisiontree_model.pkl'),
    'Random_forest':joblib.load('randomfor_model.pkl')
}

st.title("HEART FAILURE PREDICTION:heart:")
st.write("In This dataset we are going to create a model on predicting the heart failure.")


#image
# image=Image.open(r"C:\Users\varma\OneDrive\Desktop\Heart Failure Project\heart.jpg")
# st.image(image,caption="Heart",use_column_width=True)


left_col,right_col=st.columns(2)

with left_col:
    age=st.text_input("Your Age")
    platelets=st.number_input("platelets, enter num in lakhs")
    creatinine_phosphokinase=st.number_input("creatinine, enter any number b/w 50 to 100")
    ejection_fraction=st.number_input("ejection_fraction,Enter any number b/w 20 to 80")
    serum_sodium=st.number_input("serum_sodium, Enter num b/w 100 to 200")
    time=st.number_input("Time, Enter any num")

with right_col:
    anaemia=st.selectbox('Anaemia, select 0-No or 1-YES',(['0','1']))
    diabetes=st.selectbox('Diabetes, select 0-No or 1-YES',(['0','1']))
    high_blood_pressure=st.selectbox('blood_pressure, select 0-No or 1-YES',(['0','1']))
    serum_creatinine=st.number_input("serum_creatinine, enter num b/w 0 to 5 in dec")
    sex=st.selectbox('GENDER, select 0-Male or 1-Female',(['0','1']))
    smoking=st.selectbox('Smoking, select 0-No or 1-YES',(['0','1']))

#model selection
model_choice=st.selectbox("Choose a model",list(models.keys()))

#predict button
if st.button("Predict"):
    input_data=pd.DataFrame({
        'age': [age],
        'anaemia': [anaemia],
        'creatinine_phosphokinase': [creatinine_phosphokinase],
        'diabetes': [diabetes],
        'ejection_fraction': [ejection_fraction],
        'high_blood_pressure': [high_blood_pressure],
        'platelets': [platelets],
        'serum_creatinine': [serum_creatinine],
        'serum_sodium': [serum_sodium],
        'sex': [sex],
        'smoking': [smoking],
        'time': [time]
        # 'Death_event': [Death_event]
    })
    model=models[model_choice]
    prediction=model.predict(input_data)
    pred_prob=model.predict_proba(input_data)

# Display the result
    if prediction[0] == 0:
        st.success(f"The model predicts that the patient will survive. Probability of survival: {pred_prob[0][0]:.2f}")
        image=Image.open(r"C:\Users\varma\OneDrive\Desktop\Heart Failure Project\healthy heart.jpeg")
        st.image(image,caption="Healthy Heart",width=500)
    else:
        st.error(f"The model predicts that the patient will not survive. Probability of death: {pred_prob[0][1]:.2f}")
        image=Image.open(r"C:\Users\varma\OneDrive\Desktop\Heart Failure Project\Failured heart.jpeg")
        st.image(image,caption="Failured Heart",width=500)
