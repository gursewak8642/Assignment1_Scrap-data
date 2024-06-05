from bs4 import BeautifulSoup
import requests
import psycopg2

url = 'https://groww.in/indices'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
data=[]

table = soup.find('table')
rows = table.find_all('tr')
headers = [header.text.strip() for header in rows[0].find_all('th')]

data.append(headers)
        
for row in rows[1:]:
    columns = row.find_all('td')
    columns_data = [column.text.strip() for column in columns]
    data.append(columns_data)
    
connection = psycopg2.connectionect(
    dbname="scrap_data",
    user="postgres",
    password="krishna",
    host="localhost"
)
if(connection is not None):
    print("connectionected to the PostgreSQL database")

cursor = connection.cursor()
create_table_query = """
CREATE TABLE IF NOT EXISTS Companies (
                Index_Name VARCHAR(255) PRIMARY KEY,
                Last_Traded VARCHAR(255),
                Day_change VARCHAR(255), 
                High VARCHAR(255), 
                Low VARCHAR(255),
                Open VARCHAR(255), 
                Prev_close VARCHAR(255)
);
"""

# Execute SQL query to create table
cursor.execute(create_table_query)
print("Table 'Companies' created or already exists")

sample = []

for prop in data[1:]:  # Skip header
    Index_Name, Last_Traded, Day_change, High, Low, Open, Prev_close = prop
    sample.append({"Index_Name": Index_Name, "Last_Traded": Last_Traded, "Day_change": Day_change, "High": High, "Low": Low, "Open": Open, "Prev_close": Prev_close})

for col in sample:
    cursor.execute("""
        INSERT INTO companies (Index_Name, Last_Traded, Day_change, High, Low, Open, Prev_close)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (Index_Name) 
        DO UPDATE SET 
            Last_Traded = EXCLUDED.Last_Traded,
            Day_change = EXCLUDED.Day_change,
            High = EXCLUDED.High,
            Low = EXCLUDED.Low,
            Open = EXCLUDED.Open,
            Prev_close = EXCLUDED.Prev_close;
        """, (col['Index_Name'], col['Last_Traded'], col['Day_change'], col['High'], col['Low'], col['Open'], col['Prev_close']))

connection.commit()
print("Data inserted or updated successfully")

cursor.close()
connection.close()
