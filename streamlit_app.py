
import streamlit

streamlit.title('This is my first new application in streamlit')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


import pandas as pd

my_fruit_list= pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list= my_fruit_list.set_index('Fruit')



selected_fruits=streamlit.multiselect("Pick some fruits: ",list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show= my_fruit_list.loc[selected_fruits]

streamlit.dataframe(fruits_to_show)
