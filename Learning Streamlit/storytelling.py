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

exercise21.drop(exercise21.index[6], inplace=True)

chart = alt.Chart(exercise21).mark_bar().encode(
    y = alt.Y('value:Q', axis=alt.Axis(title='%')),
    x=alt.X('variable:N', axis=alt.Axis(title=None, labels = False)),
    color=alt.Color('variable:N', legend=alt.Legend(title='Metric')),
    column=alt.Column('Tier:O', header=alt.Header(labelOrient='bottom'),
                      sort = ['A+',  'A', 'B', 'C', 'D', 'All other', 'Total'])
).transform_fold(
    fold = ['% Accounts', '% Revenue'],
    as_=['variable', 'value']
)

st.altair_chart(chart, use_container_width=False)

# Your dataframe and chart setup code here...

# Create a line chart to connect the bars
line_data = []

for i in range(len(exercise21)):
    tier = exercise21.loc[i, 'Tier']
    accounts = exercise21.loc[i, '% Accounts']
    revenue = exercise21.loc[i, '% Revenue']
    
    line_data.append({'Tier': tier, 'variable': '% Accounts', 'value': accounts, 'next_variable': '% Revenue', 'next_value': revenue})
    line_data.append({'Tier': tier, 'variable': '% Revenue', 'value': revenue, 'next_variable': '% Accounts', 'next_value': accounts})

line_df = pd.DataFrame(line_data)

st.write(line_df)
# Create the line chart
line_chart = alt.Chart(line_df).mark_line().encode(
    x=alt.X('Tier:N', axis=alt.Axis(title='Tier'), sort=None),
    y=alt.Y('value:Q', axis=alt.Axis(title='Percentage')),
    color=alt.Color('variable:N', legend=alt.Legend(title='Metric')),
    detail='variable:N'
)
# Create the bar chart
bar_chart = alt.Chart(exercise21).mark_bar().encode(
    alt.X('Tier', sort=None),
    y=alt.Y('% Accounts', axis=alt.Axis(title='%')),
    color=alt.Color('variable:N', legend=alt.Legend(title='Metric')),
    xOffset=alt.Column('variable:N', title=None)
).transform_fold(
    ['% Accounts', '% Revenue'],
    as_=['variable', 'value']
)

# Combine the bar chart and line chart
chart4 = alt.layer(
    bar_chart,
    line_chart
).properties(
    width=400  # Adjust the width of the chart as needed
)

st.altair_chart(chart3)



st.altair_chart(chart4)
