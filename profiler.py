import streamlit as st

st.title('Personal Profile Dashboard')

name = st.text_input("Enter Your Name", "Type Here ...")

gender = st.radio("Select Gender:", ('Male', 'Female'))

if gender == 'Male':
    st.success("Gender selected: Male")
else:
    st.success("Gender selected: Female")

hobby = st.selectbox("Select a Hobby:", ['Dancing', 'Reading', 'Sports'])
st.write("Your selected hobby is:", hobby)

additional_hobbies = st.multiselect("Select Additional Hobbies:", ['Dancing', 'Reading', 'Sports'])
st.write("You selected", len(additional_hobbies), "additional hobbies:", ', '.join(additional_hobbies))

show_info = st.checkbox("Check this box to show additional information")

if show_info:
    st.text("You checked the box! Here is some additional information.")
    st.text("Feel free to explore the features below.")

level = st.slider("Select Your Fitness Level:", 1, 5)
st.text(f'Selected Fitness Level: {level}')

if st.button('Submit Profile'):
    if name:
        st.success(f"Profile submitted! Name: {name}, Gender: {gender}, Hobby: {hobby}, Fitness Level: {level}")
    else:
        st.warning("Please enter your name.")

if st.button("About"):
    st.text("Welcome to the Personal Profile Dashboard!")

if st.button('Display Name'):
    if name:
        st.success(f"Your name is: {name.title()}")
    else:
        st.warning("Please enter your name to display it.")

if st.button("Click me for no reason"):
    st.text("This button does nothing specific, but thanks for clicking it!")
