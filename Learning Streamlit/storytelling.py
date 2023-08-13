"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('Storytelling with Data!')


st.write('This streamlit app is meant to learn how to use streamlit and practice the examples in the book *Storytelling with Data - Lets Practice!*')

st.header('Exercise 2.1 - Improve this table')

st.write('Starting table:')

exercise21 = pd.read_excel(r"C:\Users\maisa\Downloads\2.1-EXERCISE.xlsx")

st.dataframe(exercise21)

st.write("Now the following fixes are suggested by the book:")
st.markdown("* Tiers not ordered")
st.markdown("* Doesn't have a total")
st.markdown("* Total not summing 100%")
st.markdown("* Round numbers and percentage")

st.write("This is the new table:")

exercise21 = exercise21.loc[[1, 0, 2, 3, 4]]
exercise21['% Accounts'] = exercise21['% Accounts'].apply(lambda x: x*100)
exercise21['% Revenue'] = exercise21['% Revenue'].apply(lambda x: x*100)

other_account_per = 100 - exercise21['% Accounts'].sum()
other_revenue_per = 100 - exercise21['% Revenue'].sum()

other_account_num = (other_account_per*exercise21['# of Accounts'][0])/exercise21['% Accounts'][0]
other_revenue_num = (other_revenue_per*exercise21['Revenue ($M)'][0])/exercise21['% Revenue'][0]


exercise21.loc[len(exercise21)] = ["All other", other_account_num, other_account_per, other_revenue_num, other_revenue_per]

exercise21.loc[len(exercise21)] = ["Total", exercise21['# of Accounts'].sum(), exercise21['% Accounts'].sum(), exercise21['Revenue ($M)'].sum(), exercise21['% Revenue'].sum()]


exercise21['% Accounts'] = exercise21['% Accounts'].apply(lambda x: round(x))
exercise21['Revenue ($M)'] = exercise21['Revenue ($M)'].apply(lambda x: round(x, 1))

st.dataframe(exercise21)

st.write("*Note*: I will not be putting the symbols $ or % like the example shown in the book as it would turn the numbers into strings.")

st.write("The author then tweaks the table a little more, adding coloring to the cells; since my project does not focus on tables, I will not do this exercise.")

teste = alt.Chart(exercise21).mark_bar().encode(
    x='Tier',
    y='% Accounts'
)

st.write(teste)