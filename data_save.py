import psycopg2

# DATABASE DETAILS
hostname="localhost"
database="scrap_data"
username="postgres"
pwd="krishna"
port_id=5432


def save(data):
    try:
        # connectionECTING DAGTABASE
        connection= psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
        )
# CREATING TABLE IN DATABASE
        cursor = connection.cursor()
        cursor.execute('DROP TABLE IF EXISTS companies')
        create_table='''CREATE TABLE IF NOT EXISTS properties(
                            Index_Name VARCHAR(255) PRIMARY KEY,
                            Last_Traded VARCHAR(255),
                            Day_change VARCHAR(255), 
                            High VARCHAR(255), 
                            Low VARCHAR(255),
                            Open VARCHAR(255), 
                            Prev_close VARCHAR(255)       )'''
        cursor.execute(create_table)
    # INSERTING DATA TO DATABASE
        insert_data = 'INSERT INTO companies (Index_Name,Last_Traded,Day_change,High,Low,Open, prev_close) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        for item in data:
            # print(item)
            insert_values=item
            cursor.execute(insert_data,insert_values)
        connection.commit()
        print("added succesfully")

    except Exception as error:
        print(error)


