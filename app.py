import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

conn_string = 'mysql+pymysql://herofinder:notanseguro@127.0.01/hero_data'

def get_hero_profile(hero_name):
    engine = create_engine(conn_string)
    data = pd.read_sql(
        sql="SELECT * FROM heroes WHERE name LIKE '%{}%'".format(hero_name),
        con=engine
    )
    return data

def plot_by_alignment(heroes_data):
    data = heroes_data[['name','Alignment']].groupby(['Alignment']).agg(['count'])
    return data

def plot_by_gender(heroes_data):
    data = heroes_data[['name','Gender']].groupby(['Gender']).agg(['count'])
    return data

def main():
    st.title('Hero Finder')
    hero_name = st.text_input('Hero name')
    search = st.button('Search')
    if search:
        hero_profile = get_hero_profile(hero_name)
        alignment = plot_by_alignment(hero_profile)
        gender = plot_by_gender(hero_profile)
        st.write(hero_profile)
        st.bar_chart(alignment['name'])
        st.bar_chart(gender['name'])

if __name__ == '__main__':
    main()