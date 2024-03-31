import pandas as pd
import sqlite3

def create_database():
    countries_to_continent = pd.read_csv('data/countries_to_continent.csv')
    covid_confirmed = pd.read_csv('data/covid_confirmed.csv')
    covid_recovered = pd.read_csv('data/covid_recovered.csv')

    # Reshape the data to long format
    covid_confirmed_melted = pd.melt(covid_confirmed, 
                                    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
                                    var_name='Date', 
                                    value_name='Confirmed')

    covid_recovered_melted = pd.melt(covid_recovered, 
                                    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
                                    var_name='Date', 
                                    value_name='Recovered')

    covid_confirmed_melted['Date'] = pd.to_datetime(covid_confirmed_melted['Date']).dt.strftime('%Y-%m-%d')
    covid_recovered_melted['Date'] = pd.to_datetime(covid_recovered_melted['Date']).dt.strftime('%Y-%m-%d')

    covid_confirmed_melted.rename(columns = {'Province/State':'province_state', 
                                            'Country/Region':'country_region',
                                            'Lat':'lat',
                                            'Long':'long',
                                            'Date': 'date',
                                            'Confirmed': 'confirmed'}, inplace=True)
    covid_recovered_melted.rename(columns = {'Province/State':'province_state', 
                                            'Country/Region':'country_region',
                                            'Lat':'lat',
                                            'Long':'long',
                                            'Date': 'date',
                                            'Recovered': 'recovered'}, inplace=True)
    countries_to_continent.rename(columns={'Continent':'continent', 'Country':'country'}, inplace=True)

    # Establish a connection to the SQLite database
    conn = sqlite3.connect('covid_data.db')
    cur = conn.cursor()

    # Create tables in the database
    try:
        cur.execute('''DROP TABLE IF EXISTS countries_to_continent''')
        cur.execute('''DROP TABLE IF EXISTS covid_confirmed''')
        cur.execute('''DROP TABLE IF EXISTS covid_recovered''')
        conn.commit()

        cur.execute('''CREATE TABLE IF NOT EXISTS countries_to_continent (
                        continent TEXT,
                        country TEXT,
                        PRIMARY KEY (continent, country)
                    )''')

        cur.execute('''CREATE TABLE IF NOT EXISTS covid_confirmed (
                        province_state TEXT,
                        country_region TEXT,
                        lat REAL,
                        long REAL,
                        date TEXT,
                        confirmed INTEGER,
                        FOREIGN KEY (country_region) REFERENCES countries_to_continent(country)
                    )''')

        cur.execute('''CREATE TABLE IF NOT EXISTS covid_recovered (
                        province_state TEXT,
                        country_region TEXT,
                        lat REAL,
                        long REAL,
                        date TEXT,
                        recovered INTEGER,
                        FOREIGN KEY (country_region) REFERENCES countries_to_continent(country)
                    )''')
        # Insert data into the tables
        countries_to_continent.to_sql('countries_to_continent', conn, if_exists='append', index=False)
        covid_confirmed_melted.to_sql('covid_confirmed', conn, if_exists='append', index=False)
        covid_recovered_melted.to_sql('covid_recovered', conn, if_exists='append', index=False)

        # Commit changes and close connection
        conn.commit()
        conn.close()

        print("Data has been successfully imported into the SQLite database.")
    except Exception as e:
        print("An error occurred:", e)
