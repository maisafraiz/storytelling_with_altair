"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('Storytelling with Data!')


st.write('This streamlit app is meant to learn how to use streamlit/altair and practice the examples in the book *Storytelling with Data - Lets Practice!*')

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

rounded_ver = exercise21.copy()

rounded_ver['% Accounts'] = exercise21['% Accounts'].apply(lambda x: round(x))
rounded_ver['Revenue ($M)'] = exercise21['Revenue ($M)'].apply(lambda x: round(x, 1))

st.dataframe(rounded_ver)

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
).properties(title={
      "text": ["New client tier share"], 
      "subtitle": ["% OF TOTAL ACCOUNTS vs REVENUE"],
      "subtitleColor": "blue"
    }
)

st.altair_chart(chart, use_container_width=False)

st.caption("Note to self: I've been finding really difficult to translate some examples of the books, as I feel some things are easy in Excel but I cannot find similar documentation for it in Altair.")

st.header('Backing up - learning Altair')

st.write('Due to difficulties adapting Excel graphs to Altair, I\'ll do a quick tutorial on the library.')

st.caption("First note: always work with tidy data - where each variable is a column, each observation is a row, and each type of observational unit is a table. This will make your life easier.")

st.write("**Chart object:**")

st.code("chart = alt.Chart(data)")

st.write("**Mark attribute:**")

st.write("Pie chart:")
st.code("alt.Chart(data).mark_arc()")

st.write("Filled area plot:")
st.code("alt.Chart(data).mark_area()")

st.write("Bar plot:")
st.code("alt.Chart(data).mark_bar()")

st.write("Scatter plot with circles:")
st.code("alt.Chart(data).mark_circle()")

st.write("Geographic:")
st.code("alt.Chart(data).mark_geoshape()")

st.write("Scatter plot with image markers:")
st.code("alt.Chart(data).mark_image()")

st.write("Line plot:")
st.code("alt.Chart(data).mark_line()")

st.write("Scatter plot with point shapes:")
st.code("alt.Chart(data).mark_point()")

st.write("Filled rectangle:")
st.code("alt.Chart(data).mark_rec()")

st.write("Line spanning the axis:")
st.code("alt.Chart(data).mark_rule()")

st.write("Scatter plot with squares:")
st.code("alt.Chart(data).mark_square()")

st.write("Scatter plot with text:")
st.code("alt.Chart(data).mark_text()")

st.write("Tick mark:")
st.code("alt.Chart(data).mark_tick()")

st.write("Line with variable width:")
st.code("alt.Chart(data).mark_trail()")

st.write("Box plot:")
st.code("alt.Chart(data).mark_boxplot()")

st.write("Continuous band around a line:")
st.code("alt.Chart(data).mark_errorband()")

st.write("Errorbar around a point:")
st.code("alt.Chart(data).mark_errorbar()")