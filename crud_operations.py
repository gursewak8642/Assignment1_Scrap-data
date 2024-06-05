import psycopg2

# Database connection details (modify these with your credentials)
hostname = "localhost"
database = "scrap_data"
username = "postgres"
pwd = "krishna"
port_id = 5432

def connect():
    """
    Connects to the PostgreSQL database.
    Returns a psycopg2 connection object or None on failure.
    """
    try:
        connection = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        )
        return connection
    except Exception as error:
        print("Error connecting to database:", error)
        return None

def create_cursor(connection):
    """
    Creates a cursor object from the provided connection.
    Returns a psycopg2 cursor object or None on failure.
    """
    if connection:
        try:
            return connection.cursor()
        except Exception as error:
            print("Error creating cursor:", error)
            return None
    else:
        print("Connection not established. Cannot create cursor.")
        return None

def close_connection(connection):
    """
    Closes the database connection if it's open.
    """
    if connection:
        try:
            connection.close()
        except Exception as error:
            print("Error closing database connection:", error)

def insert(data):
    """
    Inserts a new record into the 'companies' table.
    Checks for duplicate Index_Name before insertion.

    Args:
        data (list): A list containing values to be inserted in the same
                     order as the table columns.
    """
    connection = connect()
    cursor = create_cursor(connection)

    if connection and cursor:
        try:
            # Check if record exists (prevents duplicate Index_Name)
            check_query = "SELECT * FROM companies WHERE Index_Name = %s"
            cursor.execute(check_query, (data[0],))
            existing_record = cursor.fetchone()

            if not existing_record:
                # Insert data if record doesn't exist
                insert_data = 'INSERT INTO companies (Index_Name, Last_Traded, Day_change, High, Low, Open, Prev_close) VALUES (%s,%s,%s,%s,%s,%s,%s)'
                insert_values = data
                cursor.execute(insert_data, insert_values)
                connection.commit()
                print("Data added successfully")
            else:
                print(f"Record with Index_Name '{data[0]}' already exists. Skipping insertion.")

        except Exception as error:
            print("Got an Error:", error)
        finally:
            close_connection(connection)


def select_all():
    """
    Fetches all data from the 'companies' table.
    Prints retrieved data or a message if no data is found.
    """
    connection = connect()
    cursor = create_cursor(connection)

    if connection and cursor:
        try:
            # Fetch all data from companies table
            select_query = "SELECT * FROM companies"
            cursor.execute(select_query)
            rows = cursor.fetchall()

            # Print retrieved data
            if rows:
                for row in rows:
                    print(row)
            else:
                print("No data found in companies table.")

        except Exception as error:
            print("Got an Error:", error)
        finally:
            close_connection(connection)

def update(data):
    """
    Updates existing data based on the provided Index_Name.

    Args:
        data (list): A list containing values to be updated in the same
                     order as the table columns. The first element should
                     be the Index_Name of the record to update.
    """
    connection = connect()
    cursor = create_cursor(connection)

    if connection and cursor:
        try:
            # Update data based on existing Index_Name
            update_query = """UPDATE companies 
                              SET Last_Traded = %s, Day_change = %s, High = %s, Low = %s, Open = %s, Prev_close = %s
                              WHERE Index_Name = %s """
            update_values = data[1:] + [data[0]]  # Extract the index and append it at the end for the WHERE clause
            cursor.execute(update_query, update_values)
            connection.commit()
            print("Data updated successfully")

        except Exception as error:
            print("Got an Error:", error)
        finally:
            close_connection(connection)


def delete(index_name):
    """
    Deletes a record from the 'companies' table based on the provided Index_Name.

    Args:
        index_name (str): The Index_Name value of the record to delete.
    """
    connection = connect()
    cursor = create_cursor(connection)

    if connection and cursor:
        try:
            # Delete data based on Index_Name
            delete_data = 'DELETE FROM companies WHERE Index_Name = %s'
            cursor.execute(delete_data, (index_name,))
            connection.commit()
            print("Data deleted successfully")

        except Exception as error:
            print("Got an Error:", error)
        finally:
            close_connection(connection)



# Example data (replace with your actual data)
new_data = ["new_index_name", "120", "20", "130", "110", "125", "115"]
insert(new_data)



select_all()

# Example data (replace with actual values)
updated_data = ["NIFTY 5004 Jun, 03:31 PM", "135", "25", "140", "122", "130", "120"]
update(updated_data)
select_all()
# Assuming 'Index_Name' should only be the index value (e.g., "NIFTY 5004")
index_name = "new_index_name"  # Extract the index value from the first element (modify as needed)
update_data = [index_name, "135", "25", "140", "122", "130", "120"]  # Update with extracted index and remaining data

# update(update_data)
select_all()


# Example data (replace with actual values)
index_name = "new_index_name"
update_data = [index_name, "135", "25", "140", "122", "130", "120"]  # Update with the correct values

update(update_data)
select_all()



# # Call the delete function
delete("NIFTY 5004 Jun, 03:31 PM")
# print("Record deleted successfully (if successful)")  # Optional message


select_all()




