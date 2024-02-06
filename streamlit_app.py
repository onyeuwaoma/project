"""
Created on Mon Feb  5 11:36:42 2024

In this project I used the data from NASA AERONET site at Simeonstown.
The data are mainly aerosol parameters.

First I installed streamlit from the bash using "pip install streamlit"
"""


import streamlit as st
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path, delimiter=';', decimal=',')

def main():
    st.title("Showcasing my Research Using the Streamlite App")

    # Load your data
data_file_path = 'mydata.csv'
df = load_data(data_file_path)
print(data_file_path)
print(df)
    # Display the data
st.write("Data_app:", df)

    # Add other visualizations or information about your research
    # For example, you can use st.line_chart, st.bar_chart, st.map, etc.

if __name__ == "__main__":
    main()























