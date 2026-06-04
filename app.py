import pickle
import streamlit as st

model = pickle.load(open("linear_model.pkl","rb"))
scaler = pickle.load(open("scaler.pkl","rb"))

import pandas as pd

# User Inputs
age = int(input("Enter Age: "))

sex = input("Enter Sex (Male/Female): ")

bmi = float(input("Enter BMI: "))

children = int(input("Enter Number of Children: "))

smoker = input("Smoker? (Yes/No): ")

region = input("Enter Region (northeast/northwest/southeast/southwest): ")

if bmi < 18.5:
    bmi_category = "Under Weight"
elif bmi < 25:
    bmi_category = "Healthy Weight"
elif bmi < 30:
    bmi_category = "Over Weight"
elif bmi < 35:
    bmi_category = "Obese"
elif bmi < 40:
    bmi_category = "Heavy Obese"
else:
    bmi_category = "Morbidly Obese"

input_data = pd.DataFrame({
    'age': [age],
    'sex': [1 if sex.lower() == 'male' else 0],
    'bmi': [bmi],
    'children': [children],
    'smoker': [1 if smoker.lower() == 'yes' else 0],

    'region_northeast': [1 if region.lower() == 'northeast' else 0],
    'region_northwest': [1 if region.lower() == 'northwest' else 0],
    'region_southeast': [1 if region.lower() == 'southeast' else 0],
    'region_southwest': [1 if region.lower() == 'southwest' else 0],

    'bmi_category_Healthy Weight': [1 if bmi_category == 'Healthy Weight' else 0],
    'bmi_category_Heavy Obese': [1 if bmi_category == 'Heavy Obese' else 0],
    'bmi_category_Morbidly Obese': [1 if bmi_category == 'Morbidly Obese' else 0],
    'bmi_category_Obese': [1 if bmi_category == 'Obese' else 0],
    'bmi_category_Over Weight': [1 if bmi_category == 'Over Weight' else 0],
    'bmi_category_Under Weight': [1 if bmi_category == 'Under Weight' else 0]
})

input_data[['age', 'bmi', 'children']] = scaler.transform(
    input_data[['age', 'bmi', 'children']]
)

prediction = model.predict(input_data)

print("Predicted Insurance Charges:", round(prediction[0].item(),2),"Rs.")