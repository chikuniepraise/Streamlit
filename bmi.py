import streamlit as st

st.title('Welcome to BMI Calculator')

weight = st.number_input("Enter your weight (in kgs)")

status = st.radio('Select your height format: ', ('cms', 'meters', 'feet'))

if status == 'cms':
    height = st.number_input('Enter your height (in centimeters)')
    try:
        bmi = weight / ((height / 100) ** 2)
    except ZeroDivisionError:
        st.text("Height cannot be zero.")
elif status == 'meters':
    height = st.number_input('Enter your height (in meters)')
    try:
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        st.text("Height cannot be zero.")
else:
    height = st.number_input('Enter your height (in feet)')
    try:
        bmi = weight / ((height / 3.28) ** 2)
    except ZeroDivisionError:
        st.text("Height cannot be zero.")

if st.button('Calculate BMI'):
    st.text(f"Your BMI Index is {bmi:.2f}.")

    if bmi < 16:
        st.error("You are Extremely Underweight")
    elif 16 <= bmi < 18.5:
        st.warning("You are Underweight")
    elif 18.5 <= bmi < 25:
        st.success("Healthy")
    elif 25 <= bmi < 30:
        st.warning("Overweight")
    else:
        st.error("Extremely Overweight")
