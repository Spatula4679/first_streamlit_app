
import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError

streamlit.title("My Mom's New Healthy Diner")
streamlit.header("Breakfast Favourites") 
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Lemon'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the picked list only in the table

streamlit.dataframe(fruits_to_show)

#new section indicates fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice: 
       streamlit.error("Please select a fruit for information.")
   else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice) 
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
      streamlit.error()
#import snowflake.connector

streamlit.header("View Our Fruit List - Add Your Favourites! ")
#snowflake-related funtions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
       my_cur.execute("SELECT * from fruit_load_list")
       return my_cur.fetchall()
       
#add a button for loading fruit
if streamlit.button('Get Fruit List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   my_cnx.close()
   streamlit.dataframe(my_data_rows)

#allow the user to add a fruit to the list
def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into fruit_load_list values ('"+new_fruit+"')")
      return "Thanks for adding " + new_fruit

   
add_my_fruit = streamlit.text_input('What fruit would you like add?')
if streamlit.button('Add A Fruit To The List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_funtion= insert_row_snowflake(add_my_fruit)
   my_cnx.close()
   streamlit.text(back_from_funtion)
  
   





 
