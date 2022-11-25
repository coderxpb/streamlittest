import streamlit as st

st.write("""
# Addition
""")
#Get Input

st.header('User Input Parameters')

def user_data():

    n1 = st.number_input("Enter number 1: ")
    n2 = st.number_input("Enter number 2: ")


    data = {'number1': n1,
            'number2': n2,
            }

    return data

dt = user_data()

st.subheader('User Input parameters')
st.write(dt)



numsum = dt['number1'] + dt['number2']
st.subheader("Sum")
st.write(numsum)


