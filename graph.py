import streamlit as st
import plotly.express as px
import sqlite3

st.title("Graph Between Date and Temperature: ")

connection = sqlite3.connect("date_temps")
cursor = connection.cursor()
cursor.execute("SELECT date FROM scrape")
dates = cursor.fetchall()
dates = [date[0] for date in dates]

cursor.execute("SELECT temperature FROM scrape")
temps = cursor.fetchall()
temps = [temp[0] for temp in temps]

figure = px.line(x=dates,
                 y=temps,
                 labels={"x": "Date",
                         "y": "Temperature (°C)"})

st.plotly_chart(figure)