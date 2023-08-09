"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np

st.title('Storytelling with Data!')


st.write('This streamlit app is meant to learn how to use streamlit and practice the examples in the book *Storytelling with Data - Lets Practice!*')

st.header('Exercise 2.1 - Improve this table')

st.write('Starting table:')

exercise21 = pd.read_excel(r"C:\Users\maisa\Downloads\2.1-EXERCISE.xlsx")

st.table(exercise21)

st.write("Now the following fixes are suggested by the book:")
st.markdown("* Tiers not ordered")
st.markdown("* Total not summing 100%")
st.markdown("* Round numbers")

st.write("This is the new table:")

exercise21 = exercise21[[cols]]