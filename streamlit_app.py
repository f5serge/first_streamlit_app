import streamlit
import pandas

streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 4 Oatmeal')
streamlit.text('Kale, Spinach Smoothie')
streamlit.text('Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
