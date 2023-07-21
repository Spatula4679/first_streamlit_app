
import streamlit
streamlit.title("My Mom's New Healthy Diner")
streamlit.header("Breakfast Favourites")
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Lemon'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the picked list only in the table
streamlit.dataframe(fruits_to_show)

#new section indicates fruityvice api response
import requests

streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi") #separating the base url and the fruit name.
# Normalises the JSON data received
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Displays the data in a tabular format in streamlit
streamlit.dataframe(fruityvice_normalized)





 
