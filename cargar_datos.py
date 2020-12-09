import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://herofinder:notanseguro@127.0.01/hero_data')

heroes_info = pd.read_csv('heroes_information.csv')
heroes_info.to_sql(
    'heroes',
    index=False,
    con=engine
)

hero_powers = pd.read_csv('super_hero_powers.csv')
hero_powers.to_sql(
    'powers',
    index=False,
    con=engine
)