import streamlit as st
import plotly.express as px
import pandas

st.title("Graph Between Date and Temperature: ")

df = pandas.read_csv("data.txt")
figure = px.line(x=df["date"],
                 y=df["temperature"],
                 labels={"x": "Date",
                         "y": "Temperature (°C)"})

st.plotly_chart(figure)


# *********** MY WAY OF DOING ***********
# with open("data.txt", "r") as file:
#     content = file.readlines()
#
# date_time = []
# temps = []
#
# datas = content[1:]
# for data in datas:
#     arr = data.strip("\n").split(",")
#     date_time.append(arr[0])
#     temps.append(arr[1])
#
# graph = px.line(x=datas,
#                  y=temps,
#                  labels={"x":"Date", "y": "Temperatures"})
#
# st.plotly_chart(graph)