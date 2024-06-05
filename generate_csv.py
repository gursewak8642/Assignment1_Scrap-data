import psycopg2
import csv
import os

def export_to_csv():
    try:
        connection = psycopg2.connectionect(
            host="localhost",
            dbname="scrap_data",
            user="postgres",
            password="krishna",
            port="5432"
        )
    except psycopg2.Error as e:
        print(f"Error connectionecting to database: {e}")
        return

    # Create a cursor object
    cursor = connection.cursor()

    # Execute SQL query
    cursor.execute("SELECT * FROM companies")
    # Fetch all rows
    rows = cursor.fetchall()

    # Fetch column names
    col_names = [desc[0] for desc in cursor.description]

    # Print retrieved data for verification (optional)
    print(f"Fetched data: {rows}")

    # Define folder path
    folder_path = "./exports"
    os.makedirs(folder_path, exist_ok=True)  # Ensure the directory exists

    # Define file path
    file_path = os.path.join(folder_path, "companies_data.csv")

    # Open CSV file for writing
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the header row
        writer.writerow(col_names)
        
        # Write the data rows
        writer.writerows(rows)
    
    print(f"Data successfully exported to {file_path}")

    # Close cursor and connectionection
    cursor.close()
    connection.close()

export_to_csv()
